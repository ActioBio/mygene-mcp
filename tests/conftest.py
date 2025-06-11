# tests/conftest.py
"""Shared test fixtures and configuration."""

import pytest
import pytest_asyncio
from unittest.mock import AsyncMock, MagicMock
from mygene_mcp.client import MyGeneClient


@pytest.fixture
def mock_client():
    """Create a mock MyGene client."""
    client = MagicMock(spec=MyGeneClient)
    client.get = AsyncMock()
    client.post = AsyncMock()
    return client


@pytest.fixture
def sample_gene_hit():
    """Sample gene hit from query results."""
    return {
        "_id": "1017",
        "_score": 22.757837,
        "entrezgene": 1017,
        "name": "cyclin dependent kinase 2",
        "symbol": "CDK2",
        "taxid": 9606
    }


@pytest.fixture
def sample_gene_annotation():
    """Sample full gene annotation."""
    return {
        "_id": "1017",
        "entrezgene": 1017,
        "name": "cyclin dependent kinase 2",
        "symbol": "CDK2",
        "taxid": 9606,
        "type_of_gene": "protein-coding",
        "genomic_pos": {
            "chr": "12",
            "start": 55966769,
            "end": 55972784,
            "strand": 1
        },
        "refseq": {
            "genomic": ["NC_000012.12"],
            "rna": ["NM_001798.5", "NM_052827.4"],
            "protein": ["NP_001789.2", "NP_439892.2"]
        },
        "ensembl": {
            "gene": "ENSG00000123374",
            "transcript": ["ENST00000266970", "ENST00000354056"],
            "protein": ["ENSP00000266970", "ENSP00000346022"]
        }
    }


@pytest.fixture
def sample_batch_results():
    """Sample batch query results."""
    return [
        {
            "_id": "1017",
            "_score": 22.757837,
            "entrezgene": 1017,
            "name": "cyclin dependent kinase 2",
            "query": "CDK2",
            "symbol": "CDK2",
            "taxid": 9606,
            "found": True
        },
        {
            "_id": "7157",
            "_score": 22.757837,
            "entrezgene": 7157,
            "name": "tumor protein p53",
            "query": "TP53",
            "symbol": "TP53",
            "taxid": 9606,
            "found": True
        },
        {
            "query": "INVALID_GENE",
            "found": False
        }
    ]


@pytest.fixture
def sample_metadata():
    """Sample metadata response."""
    return {
        "app_revision": "abcd1234",
        "available_fields": ["entrezgene", "symbol", "name", "taxid"],
        "build_date": "2024-01-01",
        "build_version": "20240101",
        "genome_assembly": {
            "human": "GRCh38",
            "mouse": "GRCm39"
        },
        "stats": {
            "total": 20000000,
            "human": 40000,
            "mouse": 35000
        }
    }


@pytest.fixture
def sample_species_facets():
    """Sample species facets response."""
    return {
        "total": 100,
        "hits": [],
        "facets": {
            "taxid": {
                "terms": [
                    {"term": 9606, "count": 40000},
                    {"term": 10090, "count": 35000},
                    {"term": 10116, "count": 25000},
                    {"term": 7227, "count": 15000},
                    {"term": 6239, "count": 10000}
                ]
            }
        }
    }