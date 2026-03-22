"""Transparência feature server — registers tools, resources, and prompts.

This file only registers components. Zero business logic (ADR-001 rule #4).
"""

from fastmcp import FastMCP

from .prompts import analise_despesas, auditoria_fornecedor, verificacao_compliance
from .resources import bases_sancoes, endpoints_disponiveis, info_api
from .tools import (
    buscar_contratos,
    buscar_emendas,
    buscar_licitacoes,
    buscar_sancoes,
    buscar_servidores,
    consultar_bolsa_familia,
    consultar_despesas,
    consultar_viagens,
)

mcp = FastMCP("mcp-brasil-transparencia")

# Tools
mcp.tool(buscar_contratos)
mcp.tool(consultar_despesas)
mcp.tool(buscar_servidores)
mcp.tool(buscar_licitacoes)
mcp.tool(consultar_bolsa_familia)
mcp.tool(buscar_sancoes)
mcp.tool(buscar_emendas)
mcp.tool(consultar_viagens)

# Resources (URIs without namespace prefix — mount adds "transparencia/" automatically)
mcp.resource("data://endpoints", mime_type="application/json")(endpoints_disponiveis)
mcp.resource("data://bases-sancoes", mime_type="application/json")(bases_sancoes)
mcp.resource("data://info-api", mime_type="application/json")(info_api)

# Prompts
mcp.prompt(auditoria_fornecedor)
mcp.prompt(analise_despesas)
mcp.prompt(verificacao_compliance)
