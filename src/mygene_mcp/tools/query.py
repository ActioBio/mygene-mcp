# src/mygene_mcp/tools/query.py
"""Gene query tools."""

from typing import Any, Dict, Optional
import mcp.types as types
from ..client import MyGeneClient


class QueryApi:
    """Tool for querying genes from MyGene.info API."""
    
    async def query_genes(
        self,
        client: MyGeneClient,
        q: str,
        fields: Optional[str] = "symbol,name,taxid,entrezgene",
        species: Optional[str] = None,
        size: Optional[int] = 10,
        from_: Optional[int] = None,
        sort: Optional[str] = None,
        facets: Optional[str] = None,
        facet_size: Optional[int] = 10,
        fetch_all: Optional[bool] = False,
        scroll_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Search for genes using the MyGene.info query API."""
        params = {"q": q}
        if fields:
            params["fields"] = fields
        if species:
            params["species"] = species
        # Fix: Use 'is not None' instead of truthiness check for size
        if size is not None:
            params["size"] = size
        if from_ is not None:
            params["from"] = from_
        if sort:
            params["sort"] = sort
        if facets:
            params["facets"] = facets
            params["facet_size"] = facet_size
        if fetch_all:
            params["fetch_all"] = "true"
        if scroll_id:
            params["scroll_id"] = scroll_id
        
        result = await client.get("query", params=params)
        
        return {
            "success": True,
            "total": result.get("total", 0),
            "took": result.get("took", 0),
            "hits": result.get("hits", []),
            "scroll_id": result.get("_scroll_id"),
            "facets": result.get("facets", {})
        }


QUERY_TOOLS = [
    types.Tool(
        name="query_genes",
        description="Search for genes using various query types (symbol, name, wildcards, etc.)",
        inputSchema={
            "type": "object",
            "properties": {
                "q": {
                    "type": "string",
                    "description": "Query string (e.g., 'CDK2', 'cyclin*', 'entrezgene:1017')"
                },
                "fields": {
                    "type": "string",
                    "description": "Comma-separated fields to return",
                    "default": "symbol,name,taxid,entrezgene"
                },
                "species": {
                    "type": "string",
                    "description": "Species filter (e.g., 'human', 'mouse', or taxonomy ID)"
                },
                "size": {
                    "type": "integer",
                    "description": "Number of results to return (max 1000)",
                    "default": 10
                },
                "from_": {
                    "type": "integer",
                    "description": "Starting result offset for pagination"
                },
                "sort": {
                    "type": "string",
                    "description": "Sort order for results"
                },
                "facets": {
                    "type": "string",
                    "description": "Facet fields for aggregation"
                },
                "facet_size": {
                    "type": "integer",
                    "description": "Number of facet results",
                    "default": 10
                },
                "fetch_all": {
                    "type": "boolean",
                    "description": "Fetch all results (returns scroll_id)",
                    "default": False
                },
                "scroll_id": {
                    "type": "string",
                    "description": "Scroll ID for fetching next batch"
                }
            },
            "required": ["q"]
        }
    )
]