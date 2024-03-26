# g2p3d

`g2p3d` is a Python library and command-line tool designed to interact with the G2P API provided by the Broad Institute. It allows users to retrieve mappings between protein isoforms, transcripts, and PDB structures for a gene, as well as protein feature tables for a gene.

## Installation

First, ensure that you have Python and pip installed on your system. Then, clone this repository to your local machine and navigate into the cloned directory:

```
git clone https://github.com/broadinstitute/g2p3d.git
cd g2p3d
```

To install `g2p3d`, run:

```
pip install .
```


This will install the `g2p3d` package and its dependencies.

## Usage

### As a Python Library

You can import `g2p3d` in your Python scripts to retrieve data from the G2P API directly. Here are some examples:

Getting Gene Transcript Map

```python
import g2p3d

# Get gene transcript map as a pandas dataframe
transcript_map = g2p3d.get_gene_transcript_map('BRCA1', 'P38398')
print(transcript_map[['UniProt Isoform','Ensembl Transcript Id', 'RefSeq mRNA Id']].head())

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
import g2p3d

# Get protein features as a pandas dataframe
protein_features = g2p3d.get_protein_features('BRCA1', 'P38398')
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


### As a Command-Line Tool
g2p3d can also be used as a command-line tool to retrieve information directly to your terminal or output files.

Getting Gene Transcript Map

```
g2p3d get-gene-transcript-map --geneName BRCA1 --uniprotId P38398
```

Getting Protein Features

```
g2p3d get-protein-features --geneName BRCA1 --uniprotId P38398
```

The above commands will print the results to your terminal. If you wish to save the output to a file, you can redirect the output:

```
g2p3d get-gene-transcript-map --geneName BRCA1 --uniprotId P38398 > transcript_map.tsv
g2p3d get-protein-features --geneName BRCA1 --uniprotId P38398 > protein_features.tsv
```

