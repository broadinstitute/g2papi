# g2papi
[![DOI](https://img.shields.io/badge/DOI-10.1038/s41592--024--02409--0-blue.svg)](https://doi.org/10.1038/s41592-024-02409-0)
[![PubMed](https://img.shields.io/badge/PubMed-39294369-blue.svg)](https://pubmed.ncbi.nlm.nih.gov/39294369/)

`g2papi` is a Python library and command-line tool designed to interact with the G2P API provided by the Broad Institute. It allows users to retrieve mappings between protein isoforms, transcripts, and PDB structures for a gene, as well as protein feature tables for a gene.

Access the swagger definition and endpoints at: https://g2p.broadinstitute.org/api-docs/

## How to cite
If you use this API, please cite [the paper](https://www.nature.com/articles/s41592-024-02409-0):

- *Kwon, S., Safer, J., Nguyen, D.T. et al. Genomics 2 Proteins portal: a resource and discovery tool for linking genetic screening outputs to protein sequences and structures. Nat Methods 21, 1947–1957 (2024), [https://doi.org/10.1101/2024.01.02.573913](https://doi.org/10.1101/2024.01.02.573913)*

or, if you prefer the `BibTeX` format:

```
@article{kwon_genomics_2024,
	author = {Kwon, Seulki and Safer, Jordan and Nguyen, Duyen T. and Hoksza, David and May, Patrick and Arbesfeld, Jeremy A. and Rubin, Alan F. and Campbell, Arthur J. and Burgin, Alex and Iqbal, Sumaiya},
	title = {Genomics 2 Proteins portal: a resource and discovery tool for linking genetic screening outputs to protein sequences and structures},
	journal = {Nature Methods},
	volume = {21},
	pages = {1947--1957},
	year = {2024},
	month = oct,
	issn = {1548-7105},
	doi = {10.1038/s41592-024-02409-0},
	url = {https://doi.org/10.1038/s41592-024-02409-0},
}
```

## Installation

First, ensure that you have Python and pip installed on your system.

### Installing with PyPi

```
pip install g2papi
```

### Installing from source

Clone this repository to your local machine and navigate into the cloned directory:

```
git clone https://github.com/broadinstitute/g2papi.git
cd g2papi
```

To install `g2papi`, run:

```
pip install .
```

This will install the `g2papi` package and its dependencies.

## Usage

### As a Python Library

You can import `g2papi` in your Python scripts to retrieve data from the G2P API directly. Here are some examples:

Calling the G2P3D API to get the Gene-Transcript-Protein Isoform-Structure mapping

```python
import g2papi

# Get gene-transcript-protein isoform-protein structure map as a pandas dataframe
gene_transcript_protein_isoform_struct = g2papi.get_gene_transcript_protein_isoform_structure('BRCA1', 'P38398')
print(gene_transcript_protein_isoform_struct[['UniProt Isoform','Ensembl Transcript Id', 'RefSeq mRNA Id']].head())

```

Output:

```
  UniProt Isoform Ensembl Transcript Id RefSeq mRNA Id
0     P38398-1(*)    ENST00000357654(*)   NM_001407611
1     P38398-1(*)    ENST00000357654(*)   NM_001407616
2     P38398-1(*)    ENST00000357654(*)   NM_001407624
3     P38398-1(*)    ENST00000357654(*)   NM_001407637
4     P38398-1(*)    ENST00000357654(*)   NM_001407641
```

Getting Protein Features

```python
import g2papi

# Get protein features as a pandas dataframe
protein_features = g2papi.get_protein_features('BRCA1', 'P38398')
protein_features.fillna('-', inplace=True)
print(protein_features[[
    'residueId', 'AA',
    'AlphaFold confidence (pLDDT)', 
    'Active site (UniProt)'
]].head())

```

Output:

```
   residueId AA  AlphaFold confidence (pLDDT) Active site (UniProt)
0          1  M                            41.59                     -
1          2  D                            45.81                     -
2          3  L                            48.11                     -
3          4  S                            63.99                     -
4          5  A                            61.73                     -
```

Getting Isoform Alignment

```python
import g2papi

# Get isoform sequence alignment between canonical and alternative isoforms
isoform_alignment = g2papi.get_isoform_sequence_alignment(
    'LDLR',      # Gene name
    'P01130-1',   # Canonical isoform UniProt ID
    'P01130-2'    # Alternative isoform UniProt ID
)

# Display the first few rows
print(isoform_alignment.head())
```

Output:

```
   residueId AA Aligned residueId (P01130-2) Aligned AA (P01130-2)
1                   M           1                   M
2                   G           2                   G
3                   P           3                   P
4                   W           4                   W
5                   G           5                   G
```

### As a Command-Line Tool
g2papi can also be used as a command-line tool to retrieve information directly to your terminal or output files.

Getting Gene-Transcript-Protein Isoform-Structure Map with the G2P3D API

```
g2papi get-gene-transcript-protein-isoform-structure-map --geneName BRCA1 --uniprotId P38398
```

Getting Protein Features

```
g2papi get-protein-features --geneName BRCA1 --uniprotId P38398
```

The above commands will print the results to your terminal. If you wish to save the output to a file, you can redirect the output:

```
g2papi get-gene-transcript-protein-isoform-structure-map --geneName BRCA1 --uniprotId P38398 > transcript_map.tsv
g2papi get-protein-features --geneName BRCA1 --uniprotId P38398 > protein_features.tsv
```

## System Requirements
The package was developed and tested on Python 3.9.12, and is designed to run on a computer that can run Python3 and has a working internet connection. The library was installed and tested on Ubuntu Linux 20.04 and Mac OSX Ventura, 13.5.1. 

## Set up time (total time to set up and run: approximately 5 minutes)
Installation and execution steps run in approximately real time. 3 installation steps each run in less than 5 seconds, and execution time takes less than 5 seconds for genes with under 2000 residues.


