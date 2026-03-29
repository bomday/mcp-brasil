"""Configuração global do mcp-brasil.

Valores podem ser sobrescritos via variáveis de ambiente.
Carrega automaticamente o arquivo .env na raiz do projeto.
"""

from __future__ import annotations

import os

from dotenv import load_dotenv

load_dotenv()

# --- HTTP Client ---
HTTP_TIMEOUT: float = float(os.environ.get("MCP_BRASIL_HTTP_TIMEOUT", "30.0"))
HTTP_MAX_RETRIES: int = int(os.environ.get("MCP_BRASIL_HTTP_MAX_RETRIES", "3"))
HTTP_BACKOFF_BASE: float = float(os.environ.get("MCP_BRASIL_HTTP_BACKOFF_BASE", "1.0"))
USER_AGENT: str = os.environ.get("MCP_BRASIL_USER_AGENT", "mcp-brasil/0.1.0")

# --- Tool Discovery ---
# "bm25" (default): BM25 search transform — replaces list_tools with search_tools + call_tool
# "code_mode": Experimental CodeMode transform — search + get_tags + execute
# "none": No transform — all 154+ tools visible at once
TOOL_SEARCH: str = os.environ.get("MCP_BRASIL_TOOL_SEARCH", "bm25")

# --- Authentication ---
# When set, requires Authorization: Bearer <token> for HTTP transport.
# Leave empty/unset for local/stdio usage without auth.
MCP_BRASIL_API_TOKEN: str | None = os.environ.get("MCP_BRASIL_API_TOKEN") or None

# --- LLM Discovery (recomendar_tools) ---
ANTHROPIC_API_KEY: str = os.environ.get("ANTHROPIC_API_KEY", "")
