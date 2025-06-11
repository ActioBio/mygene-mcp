# MyGene MCP Server

A Model Context Protocol (MCP) server that exposes the [MyGene.info](https://mygene.info/) API as a set of tools for AI assistants.

## Features

- **Gene Search**: Query genes by symbol, name, or other identifiers
- **Gene Annotations**: Retrieve detailed gene information
- **Batch Queries**: Process multiple genes in a single request
- **Genomic Interval Queries**: Find genes by chromosome position
- **Metadata Access**: Get API metadata and available fields
- **Species Support**: Query genes from multiple species

## Data Available from MyGene.info

MyGene MCP Server provides access to comprehensive gene data aggregated in real-time from 30+ authoritative sources:

### Core Gene Information
- **Gene identifiers**: Entrez Gene, Ensembl, UniProt, RefSeq, HGNC, MGI, RGD, and more
- **Basic annotations**: Official symbol, name, aliases, type of gene, genomic location
- **Cross-references**: Direct mappings between all major gene databases
- **Species coverage**: Human, mouse, rat, zebrafish, fly, worm, yeast, and 20,000+ other species

### Expression Data
- **Human Protein Atlas (HPA)**: Tissue-specific expression, subcellular localization
- **GTEx**: Gene expression across human tissues
- **BioGPS**: Expression profiles across cell types and tissues
- **ExAC**: Expression data from exome aggregation

### Functional Annotations
- **Gene Ontology (GO)**: Biological process, molecular function, cellular component with evidence codes
- **Pathways**: KEGG, Reactome, WikiPathways, BioCarta, PID pathway memberships
- **Protein domains**: InterPro, Pfam, SMART domain annotations
- **Homology**: Orthologs and paralogs from HomoloGene, Ensembl Compara, PANTHER

### Clinical and Disease Data
- **Disease associations**: DisGeNET, OMIM, ClinVar disease links
- **Genetic variants**: ClinVar variants with clinical significance
- **Pharmacogenomics**: PharmGKB drug-gene interactions
- **Chemical interactions**: ChEBI, ChEMBL, DrugBank compound associations

### Advanced Query Capabilities
- **Powerful search syntax**: Wildcards (`CDK*`), field queries (`go.MF:kinase`), boolean logic (`pathway.kegg.name:"cell cycle" AND taxid:9606`)
- **Batch operations**: Query up to 1000 genes in a single request
- **Genomic interval search**: Find genes by chromosomal coordinates
- **Complex filters**: Combine multiple criteria (species, gene type, annotation presence)
- **Data export**: Export results in TSV, CSV, JSON, or XML formats

## Installation

```bash
git clone https://github.com/nickzren/mygene-mcp
cd mygene-mcp
mamba env create -f environment.yml
mamba activate mygene-mcp
```

## Usage

#### As an MCP Server

```bash
mygene-mcp
```

#### Configure with Claude Desktop

```bash
python scripts/configure_claude.py
```