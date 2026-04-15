"""Static reference data for the TCE-PA feature."""

from __future__ import annotations

import json


def endpoints_tce_pa() -> str:
    """Catálogo de endpoints disponíveis na API de Dados Abertos do TCE-PA.

    Lista o endpoint disponível com seus parâmetros e tipos de ato aceitos.
    """
    endpoints = [
        {
            "endpoint": "/v1/diario_oficial",
            "descricao": ("Publicações do Diário Oficial do TCE-PA a partir de 2018"),
            "parametros": {
                "ano": "integer (obrigatório, padrão: 2018, mínimo: 2018)",
                "mes": "integer (opcional, 1-12)",
                "numero_publicacao": "integer (opcional)",
                "tipo_ato": "string (opcional)",
            },
            "tipo_ato_valores": [
                "Atos de Pessoal para Fins de Registro",
                "Atos e Normas",
                "Contratos",
                "Convênios e Instrumentos Congêneres",
                "Licitações",
                "Outros Atos de Pessoal",
            ],
        }
    ]
    return json.dumps(endpoints, ensure_ascii=False, indent=2)
