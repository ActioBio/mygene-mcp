# MyGene MCP Server

A Model Context Protocol (MCP) server that exposes the [MyGene.info](https://mygene.info/) API as a set of tools for AI assistants.

## Features

- **Gene Search**: Query genes by symbol, name, or other identifiers
- **Gene Annotations**: Retrieve detailed gene information
- **Batch Queries**: Process multiple genes in a single request
- **Genomic Interval Queries**: Find genes by chromosome position
- **Metadata Access**: Get API metadata and available fields
- **Species Support**: Query genes from multiple species

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