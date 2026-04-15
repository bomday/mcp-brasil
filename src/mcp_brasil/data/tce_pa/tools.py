"""Tool functions for the tce_pa feature.

Rules (ADR-001):
    - tools.py NEVER makes HTTP directly — delegates to client.py
    - Returns formatted strings for LLM consumption
"""

from __future__ import annotations

from fastmcp import Context

from mcp_brasil._shared.formatting import markdown_table

from . import client
from .constants import TIPO_ATO


async def buscar_diario_oficial_pa(
    ctx: Context,
    ano: int = 2018,
    mes: int | None = None,
    tipo_ato: str | None = None,
    numero_publicacao: int | None = None,
) -> str:
    """Busca publicações no Diário Oficial do TCE-PA.

    Pesquisa atos publicados no Diário Oficial do Tribunal de Contas
    do Estado do Pará. Os dados estão disponíveis a partir de 2018.

    Args:
        ano: Ano da publicação (padrão: 2018, mínimo: 2018).
        mes: Mês (1-12, opcional).
        tipo_ato: Tipo de ato para filtrar (opcional). Valores válidos:
            "Atos de Pessoal para Fins de Registro",
            "Atos e Normas", "Contratos",
            "Convênios e Instrumentos Congêneres",
            "Licitações", "Outros Atos de Pessoal".
        numero_publicacao: Número específico da publicação (opcional).

    Returns:
        Tabela com publicações encontradas.
    """
    await ctx.info(f"Buscando Diário Oficial do TCE-PA ({ano})...")
    publicacoes = await client.buscar_diario_oficial(
        ano=ano,
        mes=mes,
        numero_publicacao=numero_publicacao,
        tipo_ato=tipo_ato,
    )

    if not publicacoes:
        return "Nenhuma publicação encontrada para os filtros informados."

    await ctx.info(f"{len(publicacoes)} publicação(ões) encontrada(s)")

    tipos_validos = "\n".join(f"  - {v}" for v in TIPO_ATO.values())
    header = (
        f"Diário Oficial do TCE-PA — {len(publicacoes)} publicação(ões) encontrada(s):\n\n"
        f"**Tipos de ato disponíveis:**\n{tipos_validos}\n\n"
    )

    rows = [
        (
            str(p.numero_publicacao) if p.numero_publicacao else "—",
            p.data_publicacao or "—",
            p.tipo_ato or "—",
            (p.publicacao[:80] + "...")
            if p.publicacao and len(p.publicacao) > 80
            else (p.publicacao or "—"),
        )
        for p in publicacoes
    ]

    return header + markdown_table(
        ["Nº Publicação", "Data", "Tipo de Ato", "Conteúdo (resumo)"],
        rows,
    )
