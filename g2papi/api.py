import requests
import pandas as pd
from io import StringIO
from importlib.metadata import version as _pkg_version

HOST = "https://g2p.broadinstitute.org"
BASE_URL = HOST + "/api/gene/{}/protein/{}/{}"
ALIGNMENT_URL = HOST + "/api/gene/{}/protein/{}/{}/alignment"

try:
    _VERSION = _pkg_version("g2papi")
except Exception:
    _VERSION = "unknown"

_HEADERS = {"User-Agent": f"g2papi-python/{_VERSION}"}


def get_gene_transcript_protein_isoform_structure(geneName, uniprotId):
    """Retrieve the gene-transcript-protein isoform-structure mapping.

    Swagger endpoint:
        GET /api/gene/{geneName}/protein/{uniprotId}/gene-transcript-protein-isoform-structure-map
        https://g2p.broadinstitute.org/api-docs/
    """
    url = BASE_URL.format(geneName, uniprotId, "gene-transcript-protein-isoform-structure-map")
    response = requests.get(url, headers=_HEADERS)
    response.raise_for_status()

    csv_data = StringIO(response.text)
    return pd.read_csv(csv_data, sep='\t')


def get_protein_features(geneName, uniprotId):
    """Retrieve the protein feature table for a gene.

    Swagger endpoint:
        GET /api/gene/{geneName}/protein/{uniprotId}/protein-features
        https://g2p.broadinstitute.org/api-docs/
    """
    url = BASE_URL.format(geneName, uniprotId, "protein-features")
    response = requests.get(url, headers=_HEADERS)
    response.raise_for_status()

    csv_data = StringIO(response.text)
    return pd.read_csv(csv_data, sep='\t')


def get_isoform_sequence_alignment(geneName, canonicalIsoformUniprotId, alignmentIsoformUniprotId):
    """Retrieve isoform sequence alignment between canonical and alternative isoforms.

    Swagger endpoint:
        GET /api/gene/{geneName}/protein/{canonicalIsoformUniprotId}/{alignmentIsoformUniprotId}/alignment
        https://g2p.broadinstitute.org/api-docs/
    """
    url = ALIGNMENT_URL.format(geneName, canonicalIsoformUniprotId, alignmentIsoformUniprotId)
    response = requests.get(url, headers=_HEADERS)
    response.raise_for_status()

    csv_data = StringIO(response.text)
    return pd.read_csv(csv_data, sep='\t')


