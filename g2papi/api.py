import requests
import pandas as pd
from io import StringIO

HOST = "https://g2p.broadinstitute.org"
BASE_URL = HOST + "/api/gene/{}/protein/{}/{}"

def get_gene_transcript_protein_isoform_structure(geneName, uniprotId):
    url = BASE_URL.format(geneName, uniprotId, "gene-transcript-protein-isoform-structure-map")
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    
    # Use StringIO to turn the response text into a file-like object
    csv_data = StringIO(response.text)
    
    return pd.read_csv(csv_data, sep='\t')


def get_protein_features(geneName, uniprotId):
    url = BASE_URL.format(geneName, uniprotId, "protein-features")
    response = requests.get(url)
    response.raise_for_status()

    csv_data = StringIO(response.text)
    return pd.read_csv(csv_data, sep='\t')

