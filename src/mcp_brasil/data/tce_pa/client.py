"""HTTP client for the TCE-PA Dados Abertos API.

Endpoints:
    GET /v1/diario_oficial → buscar_diario_oficial
"""

from __future__ import annotations

import re
from typing import Any

from mcp_brasil._shared.http_client import http_get

from .constants import DIARIO_OFICIAL_URL
from .schemas import DiarioOficial


def _strip_html(text: str) -> str:
    """Remove HTML tags from a string, preserving whitespace."""
    return re.sub(r"<[^>]+>", " ", text).strip()


async def buscar_diario_oficial(
    ano: int = 2018,
    mes: int | None = None,
    numero_publicacao: int | None = None,
    tipo_ato: str | None = None,
) -> list[DiarioOficial]:
    """Search TCE-PA Diário Oficial publications.

    Args:
        ano: Year to search (default: 2018, minimum: 2018).
        mes: Month (1-12, optional).
        numero_publicacao: Specific publication number (optional).
        tipo_ato: Filter by act type (optional). Valid values:
            "Atos de Pessoal para Fins de Registro",
            "Atos e Normas", "Contratos",
            "Convênios e Instrumentos Congêneres",
            "Licitações", "Outros Atos de Pessoal".

    Returns:
        List of Diário Oficial publications.
    """
    params: dict[str, str] = {"ano": str(ano)}
    if mes is not None:
        params["mes"] = str(mes)
    if numero_publicacao is not None:
        params["numero_publicacao"] = str(numero_publicacao)
    if tipo_ato:
        params["tipo_ato"] = tipo_ato

    data: dict[str, Any] = await http_get(DIARIO_OFICIAL_URL, params=params)

    items = data.get("data", []) if isinstance(data, dict) else data
    return [
        DiarioOficial(
            numero_publicacao=item.get("NumeroPublicacao"),
            data_publicacao=item.get("DataPublicacao", ""),
            tipo_ato=item.get("TipoAto", ""),
            publicacao=_strip_html(item.get("Publicacao", "")),
        )
        for item in items
    ]
