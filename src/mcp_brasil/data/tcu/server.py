"""TCU feature server — registers tools, resources, and prompts.

This file only registers components. Zero business logic (ADR-001 rule #4).
"""

from fastmcp import FastMCP

from .prompts import investigar_empresa_tcu
from .resources import tipos_certidoes_apf
from .tools import (
    buscar_acordaos,
    buscar_contratos_tcu,
    buscar_pedidos_congresso,
    calcular_debito_tcu,
    consultar_cadirreg,
    consultar_certidoes_apf,
    consultar_inabilitados,
    consultar_inidoneos,
)

mcp = FastMCP("mcp-brasil-tcu")

# Tools
mcp.tool(buscar_acordaos)
mcp.tool(consultar_inabilitados)
mcp.tool(consultar_inidoneos)
mcp.tool(consultar_certidoes_apf)
mcp.tool(calcular_debito_tcu)
mcp.tool(buscar_pedidos_congresso)
mcp.tool(buscar_contratos_tcu)
mcp.tool(consultar_cadirreg)

# Resources
mcp.resource("data://tipos-certidoes-apf", mime_type="application/json")(tipos_certidoes_apf)

# Prompts
mcp.prompt(investigar_empresa_tcu)
