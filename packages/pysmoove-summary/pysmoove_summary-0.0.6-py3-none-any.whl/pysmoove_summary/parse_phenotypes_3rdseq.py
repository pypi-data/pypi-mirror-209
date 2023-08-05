from argparse import ArgumentParser
import pandas as pd

def parse_arguments():
    parser = ArgumentParser(description='parse excel file of phenotypes')
    parser.add_argument('phenotypes', metavar='<xlsx>', help='Excel file containing phenotypes')
    parser.add_argument('--line', metavar='<LINE_NO>', help='Line to test')
    return parser.parse_args()


def parse_phenotypes(df):
    df['line'] = tuple(n.split('_')[0] for n in df['sample_name'])


def main():
    args = parse_arguments()
    phenotypes = pd.read_excel(args.phenotypes, sheet_name='Sheet2', index_col='seq._no.')
    parse_phenotypes(phenotypes)
    print(phenotypes['line'].unique())
    if args.line:
        print(phenotypes[phenotypes['line'] == args.line])


if __name__ == '__main__':
    main()
