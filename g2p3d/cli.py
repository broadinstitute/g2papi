import argparse
from .api import get_gene_transcript_map, get_protein_features
import sys

def main():
    parser = argparse.ArgumentParser(description='G2P3D Command Line Interface')
    subparsers = parser.add_subparsers(dest='command')

    # Sub-command for gene-transcript-map
    gt_parser = subparsers.add_parser('get-gene-transcript-map', help='Get gene transcript map')
    gt_parser.add_argument('--geneName', required=True, help='Gene name')
    gt_parser.add_argument('--uniprotId', required=True, help='Uniprot ID')

    # Sub-command for protein-features
    pf_parser = subparsers.add_parser('get-protein-features', help='Get protein features')
    pf_parser.add_argument('--geneName', required=True, help='Gene name')
    pf_parser.add_argument('--uniprotId', required=True, help='Uniprot ID')

    args = parser.parse_args()

    if args.command == 'get-gene-transcript-map':
        print(get_gene_transcript_map(args.geneName, args.uniprotId).to_csv(index=False))
    elif args.command == 'get-protein-features':
        print(get_protein_features(args.geneName, args.uniprotId).to_csv(index=False))
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()