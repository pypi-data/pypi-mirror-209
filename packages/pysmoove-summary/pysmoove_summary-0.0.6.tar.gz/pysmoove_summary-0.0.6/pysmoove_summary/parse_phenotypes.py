from argparse import ArgumentParser
import pandas as pd

def parse_arguments():
    parser = ArgumentParser(description='parse excel file of phenotypes')
    parser.add_argument('phenotypes', metavar='<xlsx>', help='Excel file containing phenotypes')
    parser.add_argument('output', metavar='<output.xlsx>', help='output of preprocessed phenotypes')
    return parser.parse_args()


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


def main():
    args = parse_arguments()
    phenotypes = parse_phenotypes(pd.read_excel(args.phenotypes, index_col='line no.'))
    phenotypes.to_excel(args.output)
    


if __name__ == '__main__':
    main()
