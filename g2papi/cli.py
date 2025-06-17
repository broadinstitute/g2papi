import argparse
from .api import get_gene_transcript_protein_isoform_structure, get_protein_features, get_isoform_sequence_alignment
import sys

def main():
    parser = argparse.ArgumentParser(description='G2P API Command Line Interface')
    subparsers = parser.add_subparsers(dest='command')

    # Sub-command for gene-transcript-map
    gt_parser = subparsers.add_parser('get-gene-transcript-protein-isoform-structure-map', help='Get gene-transcript-protein isoform-structure map')
    gt_parser.add_argument('--geneName', required=True, help='Gene name')
    gt_parser.add_argument('--uniprotId', required=True, help='Uniprot ID')

    # Sub-command for protein-features
    pf_parser = subparsers.add_parser('get-protein-features', help='Get protein features')
    pf_parser.add_argument('--geneName', required=True, help='Gene name')
    pf_parser.add_argument('--uniprotId', required=True, help='Uniprot ID')

    # Sub-command for isoform-sequence-alignment
    isa_parser = subparsers.add_parser('get-isoform-sequence-alignment', help='Get isoform sequence alignment')
    isa_parser.add_argument('--geneName', required=True, help='Gene name')
    isa_parser.add_argument('--canonicalIsoformUniprotId', required=True, help='Canonical isoform Uniprot ID')
    isa_parser.add_argument('--alignmentIsoformUniprotId', required=True, help='Alignment isoform Uniprot ID')

    args = parser.parse_args()

    if args.command == 'get-gene-transcript-protein-isoform-structure-map':
        print(get_gene_transcript_protein_isoform_structure(args.geneName, args.uniprotId).to_csv(index=False))
    elif args.command == 'get-protein-features':
        print(get_protein_features(args.geneName, args.uniprotId).to_csv(index=False))
    elif args.command == 'get-isoform-sequence-alignment':
        print(get_isoform_sequence_alignment(args.geneName, args.canonicalIsoformUniprotId, args.alignmentIsoformUniprotId).to_csv(index=False))
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
