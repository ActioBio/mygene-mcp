# MyGene MCP Server

A Model Context Protocol (MCP) server that exposes the [MyGene.info](https://mygene.info/) API as a set of tools for AI assistants.

## Features

### Core Capabilities

- **Gene Search**: Query genes by symbol, name, Entrez ID, Ensembl ID, or other identifiers
- **Gene Annotations**: Retrieve comprehensive gene information from multiple sources
- **Expression Queries**: Search genes by tissue expression or retrieve expression profiles
- **Pathway Queries**: Find genes in biological pathways or get pathway memberships
- **GO Annotations**: Search by GO terms or retrieve GO annotations with evidence codes
- **Disease Associations**: Find disease-associated genes or get gene-disease links
- **Drug/Chemical Interactions**: Search genes by drug/chemical or get interaction data
- **Ortholog/Homology**: Find orthologs across species or search homologous genes
- **Variant Information**: Retrieve genetic variants and clinical significance
- **Batch Operations**: Process up to 1000 genes in a single request
- **Genomic Interval Search**: Find genes by chromosomal coordinates
- **Advanced Queries**: Build complex queries with boolean logic and filters
- **Data Export**: Export gene lists in TSV, CSV, JSON, or XML formats

### Data Sources
- **NCBI**: Entrez Gene, RefSeq, HomoloGene
- **Ensembl**: Gene annotations, homology data
- **UniProt**: Protein annotations, GO terms
- **Human Protein Atlas (HPA)**: Tissue expression, subcellular localization
- **GTEx**: Gene expression in human tissues
- **BioGPS**: Gene expression profiles
- **ExAC**: Exome aggregation data
- **KEGG**: Pathways and disease associations
- **Reactome**: Biological pathways
- **WikiPathways**: Community pathways
- **BioCarta**: Pathway diagrams
- **NetPath**: Signal transduction pathways
- **PID**: Pathway Interaction Database
- **Gene Ontology**: Functional annotations
- **DisGeNET**: Disease-gene associations
- **ClinVar**: Clinical variants
- **OMIM**: Genetic disorders
- **PharmGKB**: Pharmacogenomics
- **DrugBank**: Drug targets
- **ChEMBL**: Bioactive compounds
- **ChEBI**: Chemical entities
- **InterPro**: Protein families and domains
- **Pfam**: Protein families
- **SMART**: Protein domains
- **PANTHER**: Gene function classification

## Quick Start

1. **Install UV**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Setup**
   ```bash
   cd mygene-mcp
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -e .
   ```

3. **Configure Claude Desktop**
   ```bash
   python scripts/configure_claude.py
   ```
   Then restart Claude Desktop.

## Usage

#### Running the Server

```bash
mygene-mcp
```

#### Development

```bash
pytest tests/ -v
```
