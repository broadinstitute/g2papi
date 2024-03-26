import requests
import pandas as pd

BASE_URL = "https://g2p.broadinstitute.org/api/gene/{}/protein/{}/{}"

def get_gene_transcript_map(geneName, uniprotId):
    url = BASE_URL.format(geneName, uniprotId, "gene-transcript-map")
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return pd.read_csv(response.text, sep='\t')

def get_protein_features(geneName, uniprotId):
    url = BASE_URL.format(geneName, uniprotId, "protein-features")
    response = requests.get(url)
    response.raise_for_status()
    return pd.read_csv(response.text, sep='\t')

