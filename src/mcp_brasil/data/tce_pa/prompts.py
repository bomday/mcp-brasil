"""Analysis prompts for the TCE-PA feature."""

from __future__ import annotations


def analisar_diario_oficial_pa(ano: int = 2024, mes: int | None = None) -> str:
    """Análise de publicações do Diário Oficial do TCE-PA.

    Guia o LLM para buscar e analisar atos publicados no Diário Oficial
    do Tribunal de Contas do Estado do Pará em um determinado período.

    Args:
        ano: Ano de referência (padrão: 2024, mínimo: 2018).
        mes: Mês específico (1-12, opcional — omita para o ano inteiro).
    """
    periodo = f"{mes:02d}/{ano}" if mes else str(ano)
    mes_param = f", mes={mes}" if mes else ""

    return (
        f"Analise as publicações do Diário Oficial do TCE-PA em {periodo}.\n\n"
        "Siga estes passos:\n\n"
        f"1. Use `buscar_diario_oficial_pa` com ano={ano}{mes_param}"
        " para obter todas as publicações.\n"
        "2. Use `buscar_diario_oficial_pa` com"
        " tipo_ato='Contratos' para filtrar contratos.\n"
        "3. Use `buscar_diario_oficial_pa` com"
        " tipo_ato='Licitações' para filtrar licitações.\n"
        "4. Use `buscar_diario_oficial_pa` com"
        " tipo_ato='Atos e Normas' para normas e resoluções.\n\n"
        "Apresente um resumo com:\n"
        "- Total de publicações por tipo de ato\n"
        "- Principais contratos e licitações publicados\n"
        "- Atos normativos relevantes (resoluções, portarias)\n"
        "- Atos de pessoal em destaque\n"
    )
