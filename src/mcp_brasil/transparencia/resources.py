"""Resources for the Transparência feature — static reference data for LLM context.

Resources expose read-only data that LLMs can pull for context.
These give LLMs knowledge of available endpoints and databases
without calling tools.
"""

from __future__ import annotations

import json

from .constants import SANCOES_DATABASES, TRANSPARENCIA_API_BASE


def endpoints_disponiveis() -> str:
    """Lista de todos os endpoints da API do Portal da Transparência disponíveis."""
    data = [
        {
            "endpoint": "contratos",
            "descricao": "Contratos federais por CPF/CNPJ do fornecedor",
            "parametros": ["cpfCnpj", "pagina"],
        },
        {
            "endpoint": "despesas/recursos-recebidos",
            "descricao": "Despesas e recursos recebidos por favorecido e período",
            "parametros": ["mesAnoInicio", "mesAnoFim", "codigoFavorecido", "pagina"],
        },
        {
            "endpoint": "servidores",
            "descricao": "Servidores públicos federais por CPF ou nome",
            "parametros": ["cpf", "nome", "pagina"],
        },
        {
            "endpoint": "licitacoes",
            "descricao": "Licitações federais por órgão e/ou período",
            "parametros": ["codigoOrgao", "dataInicial", "dataFinal", "pagina"],
        },
        {
            "endpoint": "novo-bolsa-familia-por-municipio",
            "descricao": "Dados do Novo Bolsa Família por município",
            "parametros": ["mesAno", "codigoIbge", "pagina"],
        },
        {
            "endpoint": "novo-bolsa-familia-sacado-por-nis",
            "descricao": "Dados do Novo Bolsa Família por NIS do beneficiário",
            "parametros": ["mesAno", "nis", "pagina"],
        },
        {
            "endpoint": "emendas",
            "descricao": "Emendas parlamentares por ano e/ou autor",
            "parametros": ["ano", "nomeAutor", "pagina"],
        },
        {
            "endpoint": "viagens-por-cpf",
            "descricao": "Viagens a serviço por CPF do servidor",
            "parametros": ["cpf", "pagina"],
        },
        {
            "endpoint": "ceis/cnep/cepim/ceaf",
            "descricao": "Sanções em bases federais (inidôneas, punidas, impedidas, expulsos)",
            "parametros": ["codigoSancionado", "nomeSancionado", "pagina"],
        },
    ]
    return json.dumps(data, ensure_ascii=False)


def bases_sancoes() -> str:
    """As 4 bases de sanções federais com descrição e parâmetros de consulta."""
    data = [
        {
            "sigla": key.upper(),
            "nome": db["nome"],
            "url": db["url"],
            "parametro_cpf_cnpj": db["param_cpf_cnpj"],
            "parametro_nome": db["param_nome"],
        }
        for key, db in SANCOES_DATABASES.items()
    ]
    return json.dumps(data, ensure_ascii=False)


def info_api() -> str:
    """Informações gerais sobre a API do Portal da Transparência."""
    data = {
        "nome": "API do Portal da Transparência do Governo Federal",
        "url_base": TRANSPARENCIA_API_BASE,
        "autenticacao": {
            "tipo": "API Key",
            "header": "chave-api-dados",
            "cadastro": "https://portaldatransparencia.gov.br/api-de-dados/cadastrar-email",
        },
        "limites": {
            "horario_comercial": "90 requisições/minuto (06h-23h59)",
            "horario_madrugada": "300 requisições/minuto (00h-05h59)",
        },
        "paginacao": "Parâmetro 'pagina' (1-indexed, 15 itens por página por padrão)",
        "formatos": "JSON",
    }
    return json.dumps(data, ensure_ascii=False)
