# src/mygene_mcp/server.py
"""MyGene MCP Server implementation."""

import asyncio
import json
from typing import Any, Dict, Type
import logging

from mcp.server import Server
from mcp.server.stdio import stdio_server
import mcp.types as types

from .client import MyGeneClient
from .tools import (
    QUERY_TOOLS, QueryApi,
    ANNOTATION_TOOLS, AnnotationApi,
    BATCH_TOOLS, BatchApi,
    INTERVAL_TOOLS, IntervalApi,
    METADATA_TOOLS, MetadataApi,
    EXPRESSION_TOOLS, ExpressionApi,
    PATHWAY_TOOLS, PathwayApi,
    GO_TOOLS, GOApi,
    HOMOLOGY_TOOLS, HomologyApi,
    DISEASE_TOOLS, DiseaseApi,
    VARIANT_TOOLS, VariantApi,
    CHEMICAL_TOOLS, ChemicalApi,
    ADVANCED_TOOLS, AdvancedQueryApi,
    EXPORT_TOOLS, ExportApi
)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Combine all tools
ALL_TOOLS = (
    QUERY_TOOLS +
    ANNOTATION_TOOLS +
    BATCH_TOOLS +
    INTERVAL_TOOLS +
    METADATA_TOOLS +
    EXPRESSION_TOOLS +
    PATHWAY_TOOLS +
    GO_TOOLS +
    HOMOLOGY_TOOLS +
    DISEASE_TOOLS +
    VARIANT_TOOLS +
    CHEMICAL_TOOLS +
    ADVANCED_TOOLS +
    EXPORT_TOOLS
)

# Create API class mapping
API_CLASS_MAP = {
    # Query tools
    "query_genes": QueryApi,
    "search_by_field": QueryApi,
    "get_field_statistics": QueryApi,
    # Annotation tools
    "get_gene_annotation": AnnotationApi,
    # Batch tools
    "query_genes_batch": BatchApi,
    "get_genes_batch": BatchApi,
    # Interval tools
    "query_genes_by_interval": IntervalApi,
    # Metadata tools
    "get_mygene_metadata": MetadataApi,
    "get_available_fields": MetadataApi,
    "get_species_list": MetadataApi,
    # Expression tools
    "query_genes_by_expression": ExpressionApi,
    "get_gene_expression_profile": ExpressionApi,
    # Pathway tools
    "query_genes_by_pathway": PathwayApi,
    "get_gene_pathways": PathwayApi,
    # GO tools
    "query_genes_by_go_term": GOApi,
    "get_gene_go_annotations": GOApi,
    # Homology tools
    "get_gene_orthologs": HomologyApi,
    "query_homologous_genes": HomologyApi,
    # Disease tools
    "query_genes_by_disease": DiseaseApi,
    "get_gene_disease_associations": DiseaseApi,
    # Variant tools
    "get_gene_variants": VariantApi,
    # Chemical tools
    "query_genes_by_chemical": ChemicalApi,
    "get_gene_chemical_interactions": ChemicalApi,
    # Advanced tools
    "build_complex_query": AdvancedQueryApi,
    "query_with_filters": AdvancedQueryApi,
    # Export tools
    "export_gene_list": ExportApi,
}


class MyGeneMcpServer:
    """MCP Server for MyGene.info data."""
    
    def __init__(self):
        self.server_name = "mygene-mcp"
        self.server_version = "0.2.0"
        self.mcp_server = Server(self.server_name, self.server_version)
        self.client = MyGeneClient()
        self._api_instances: Dict[Type, Any] = {}
        self._setup_handlers()
        logger.info(f"{self.server_name} v{self.server_version} initialized.")
    
    def _setup_handlers(self):
        """Register MCP handlers."""
        
        @self.mcp_server.list_tools()
        async def handle_list_tools() -> list[types.Tool]:
            """Returns the list of all available tools."""
            return ALL_TOOLS
        
        @self.mcp_server.call_tool()
        async def handle_call_tool(
            name: str, arguments: Dict[str, Any]
        ) -> list[types.TextContent]:
            """Handles a tool call request."""
            logger.info(f"Handling call for tool: '{name}'")
            
            try:
                if name not in API_CLASS_MAP:
                    raise ValueError(f"Unknown tool: {name}")
                
                api_class = API_CLASS_MAP[name]
                
                if api_class not in self._api_instances:
                    self._api_instances[api_class] = api_class()
                
                api_instance = self._api_instances[api_class]
                
                if not hasattr(api_instance, name):
                    raise ValueError(f"Tool method '{name}' not found")
                
                func_to_call = getattr(api_instance, name)
                result_data = await func_to_call(self.client, **arguments)
                
                result_json = json.dumps(result_data, indent=2)
                return [types.TextContent(type="text", text=result_json)]
            
            except Exception as e:
                logger.error(f"Error calling tool '{name}': {str(e)}", exc_info=True)
                error_response = {
                    "error": type(e).__name__,
                    "message": str(e),
                    "tool_name": name
                }
                return [types.TextContent(type="text", text=json.dumps(error_response, indent=2))]
    
    async def run(self):
        """Starts the MCP server."""
        logger.info(f"Starting {self.server_name} v{self.server_version}...")
        
        async with stdio_server() as (read_stream, write_stream):
            await self.mcp_server.run(
                read_stream, 
                write_stream,
                self.mcp_server.create_initialization_options()
            )


def main():
    """Main entry point."""
    server = MyGeneMcpServer()
    try:
        asyncio.run(server.run())
    except KeyboardInterrupt:
        logger.info("Server interrupted by user.")
    except Exception as e:
        logger.error(f"Server error: {e}")
        raise


if __name__ == "__main__":
    main()