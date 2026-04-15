"""Constants for the TCE-PA feature."""

API_BASE = "https://sistemas.tcepa.tc.br/dadosabertos/api"

# Endpoint — Diário Oficial publications (year 2018+)
DIARIO_OFICIAL_URL = f"{API_BASE}/v1/diario_oficial"

# Valid TipoAto values accepted by the API
TIPO_ATO = {
    "PESSOAL_REGISTRO": "Atos de Pessoal para Fins de Registro",
    "ATOS_NORMAS": "Atos e Normas",
    "CONTRATOS": "Contratos",
    "CONVENIOS": "Convênios e Instrumentos Congêneres",
    "LICITACOES": "Licitações",
    "OUTROS_PESSOAL": "Outros Atos de Pessoal",
}
