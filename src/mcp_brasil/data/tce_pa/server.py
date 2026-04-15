"""tce_pa feature server — registers tools, resources, and prompts.

This file only registers components. Zero business logic (ADR-001 rule #4).
"""

from fastmcp import FastMCP

from .prompts import analisar_diario_oficial_pa
from .resources import endpoints_tce_pa
from .tools import buscar_diario_oficial_pa

mcp = FastMCP("mcp-brasil-tce-pa")

# Tools
mcp.tool(
    buscar_diario_oficial_pa,
    tags={"busca", "diário-oficial", "tce", "pará"},
)

# Resources
mcp.resource("data://endpoints", mime_type="application/json")(endpoints_tce_pa)

# Prompts
mcp.prompt(analisar_diario_oficial_pa)
