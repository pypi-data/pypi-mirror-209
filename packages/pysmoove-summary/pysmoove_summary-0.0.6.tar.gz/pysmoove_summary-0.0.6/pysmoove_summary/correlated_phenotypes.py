#===============================================================================
# correlated_phenotypes.py
#===============================================================================

from argparse import ArgumentParser
from pysam import VariantFile
import statsmodels.api as sm
import pandas as pd

DHFFC_DEL = 0.7
DHFFC_DUP = 1.25
MSHQ = 3.0

def parse_phenotypes(df):
    df['yellow_leaf(yellow:1)'].fillna(0, inplace=True)
    df['curly(curly:1)'].fillna(0, inplace=True)
    df['root_width(wider:1, narrower:0)'].replace(0, -1, inplace=True)
    df['root_width(wider:1, narrower:0)'].fillna(0, inplace=True)
    df.columns = ['seq no.', 'nanopore', 'Line', 'no.Accessory_Roots',
       'Gravitropism', 'root_length',
       'yellow_leaf', 'curly',
       'root_width']
    df['root_length_fillna'] = df.loc[:,'root_length']
    df['root_length_fillna'].replace(0, -1, inplace=True)
    df['root_length_fillna'].fillna(0, inplace=True)
    return df


def parse_arguments():
    parser = ArgumentParser(description='generate summary BED from VCF of SVs')
    parser.add_argument('vcf', metavar='<vcf>', help='VCF containing SVs')
    parser.add_argument('phenotypes', metavar='<xlsx>', help='Excel file containing phenotypes')
    parser.add_argument('line', metavar='<LINE>', help='Line to test')
    parser.add_argument('phenotype', metavar='<phenotype>', help='Phenotype to test')
    parser.add_argument('output_prefix', metavar='<output_prefix>')
    parser.add_argument('--dhffc-del', metavar='<float>', type=float,
        default=DHFFC_DEL, help=f'filter out deletions with DHFFC above this value [{DHFFC_DEL}]')
    parser.add_argument('--dhffc-dup', metavar='<float>', type=float,
        default=DHFFC_DUP, help=f'filter out duplications with DHFFC below this value [{DHFFC_DUP}]')
    parser.add_argument('--mshq', metavar='<float>', type=float,
        default=MSHQ, help=f'filter out hets with MSHQ below this value [{MSHQ}]')
    parser.add_argument('--sv-only', action='store_true',
        help='show SVs only, no SNPs or small INDELs')
    return parser.parse_args()


def generate_rows(args):
    vcf_in = VariantFile(args.vcf)
    alts_set = set(f'<{a}>' for a in vcf_in.header.alts.keys())
    phenotypes = parse_phenotypes(pd.read_excel(args.phenotypes, index_col='line no.')).loc[:, args.phenotype].dropna()

    for rec in vcf_in.fetch():
        samples = sorted((s for s in rec.samples
                        if s.split('_')[0] == args.line
                        if s in phenotypes.index), key=lambda x: int(x.split('_')[1]))
        if any(any(a is None for a in rec.samples[s].allele_indices) for s in samples):
            continue
        genotypes = tuple('/'.join(str(i) for i in rec.samples[s].allele_indices) for s in samples)
        genotypes_quant = tuple(sum(rec.samples[s].allele_indices) for s in samples)
        if len(set(genotypes)) < 2:
            continue
        phenos = tuple(phenotypes.loc[s] for s in samples)
        if len(set(phenos)) < 2:
            continue
        X = sm.add_constant(genotypes_quant)
        est = sm.OLS(phenos, X)
        model = est.fit()
        if (rec.alts[0] not in alts_set):
            if not args.sv_only:
                yield (rec.contig, rec.pos-1, rec.stop, ','.join(rec.info['TYPE']),
                    rec.stop - rec.start, ','.join(samples), ','.join(genotypes),
                    ','.join(str(int(p)) for p in phenos), model.params[1],
                    model.bse[1], model.pvalues[1], 'NA')
            continue
        if rec.info['SVTYPE'] == 'BND':
            continue
        if rec.info['SVTYPE'] == 'DEL':
            if all(rec.samples[s]['DHFFC'] > args.dhffc_del for s in samples):
                continue
        if rec.info['SVTYPE'] == 'DUP':
            if all(rec.samples[s]['DHFFC'] < args.dhffc_dup for s in samples):
                continue
        if '0/1' in genotypes:
            if rec.info['MSHQ'] < args.mshq:
                continue
        genes = tuple(g.split('|')[0] for g in rec.info.get('smoove_gene', ())
                        if g.split('|')[1].startswith('gene'))
        if len(genes) == 0:
            genes = ('NA',)
        elif len(genes) > 4:
            genes = ('MANY',)
        yield (rec.contig, rec.pos-1, rec.stop, rec.info['SVTYPE'],
                abs(rec.info['SVLEN'][0]), ','.join(samples),
                ','.join(genotypes), ','.join(str(int(p)) for p in phenos),
                model.params[1], model.bse[1], model.pvalues[1],
                ','.join(genes))


def main():
    args = parse_arguments()
    correlations = pd.DataFrame(generate_rows(args), columns = ('chrom', 'start', 'stop', 'type', 'size', 'samples',
                'genotypes', 'phenotypes', 'beta', 'se', 'pvalue', 'genes'))
    correlations.sort_values('pvalue', inplace=True)
    correlations.to_csv(f'{args.output_prefix}.bed', index=False, header=False, sep='\t')
    correlations.to_excel(f'{args.output_prefix}.xlsx', index=False)

if __name__ == '__main__':
    main()
