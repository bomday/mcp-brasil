# TCU (Tribunal de Contas da Uniao) — Mapeamento Completo de APIs

Pesquisa realizada em 22/03/2026.

---

## Visao Geral

O TCU disponibiliza **10 webservices REST** abertos distribuidos em 4 dominios distintos. Todos sao **sem autenticacao**, retornam **JSON** (exceto licitacoes que usa XML) e nao documentam rate limits. Ha tambem bases de dados em **CSV** para download (jurisprudencia, normas, inidoneos/inabilitados).

**Dominios base:**
- `dados-abertos.apps.tcu.gov.br` — Acordaos, atos normativos, pautas, CADIRREG
- `contas.tcu.gov.br/ords/` — Inabilitados, inidoneos, pedidos do Congresso (Oracle REST Data Services)
- `certidoes-apf.apps.tcu.gov.br` — Certidoes consolidadas de pessoa juridica
- `divida.apps.tcu.gov.br` — Calculadora de debito
- `contas.tcu.gov.br/contrata2RS/` — Termos contratuais do TCU

**Documentacao oficial:** https://sites.tcu.gov.br/dados-abertos/webservices-tcu/

**Nota de manutencao:** Servicos podem ficar indisponiveis entre 20:00 e 21:00 diariamente.

---

## Endpoint 1: Consultar Acordaos

Acordaos (decisoes colegiadas) do TCU.

| Campo | Valor |
|-------|-------|
| **URL** | `GET https://dados-abertos.apps.tcu.gov.br/api/acordao/recupera-acordaos` |
| **Auth** | Nenhuma |
| **Status** | ATIVO (verificado 22/03/2026, HTTP 200) |

### Parametros

| Parametro | Tipo | Obrigatorio | Descricao |
|-----------|------|-------------|-----------|
| `inicio` | int | Nao | Indice inicial dos resultados (paginacao) |
| `quantidade` | int | Nao | Quantidade de registros a retornar |

### Resposta (JSON Array)

```json
[
  {
    "key": "ACORDAO-COMPLETO-2745491",
    "tipo": "ACORDAO",
    "anoAcordao": "2026",
    "titulo": "ACORDAO 691/2026 ATA 8/2026 - PLENARIO",
    "numeroAcordao": "691",
    "numeroAta": "8/2026",
    "colegiado": "Plenario",
    "dataSessao": "18/03/2026",
    "relator": "BRUNO DANTAS",
    "situacao": "OFICIALIZADO",
    "sumario": "EMBARGOS DE DECLARACAO EM PEDIDO DE RECONSIDERACAO...",
    "urlArquivo": "https://contas.tcu.gov.br/sagas/SvlVisualizarRelVotoAcRtf?...",
    "urlArquivoPdf": "https://contas.tcu.gov.br/sagas/SvlVisualizarRelVotoAc?...",
    "urlAcordao": "https://contas.tcu.gov.br/pesquisaJurisprudencia/#/detalhamento/..."
  }
]
```

### Campos da Resposta

| Campo | Tipo | Descricao |
|-------|------|-----------|
| `key` | string | Identificador unico no banco (ex: "ACORDAO-COMPLETO-2745491") |
| `tipo` | string | Tipo do documento ("ACORDAO") |
| `anoAcordao` | string | Ano do acordao |
| `titulo` | string | Titulo formatado: "TIPO NUM/ANO ATA NUM/ANO - COLEGIADO" |
| `numeroAcordao` | string | Numero do acordao |
| `numeroAta` | string | Numero/ano da ata (ex: "8/2026") |
| `colegiado` | string | Colegiado responsavel ("Plenario", "1a Camara", "2a Camara") |
| `dataSessao` | string | Data da sessao no formato DD/MM/AAAA |
| `relator` | string | Nome do ministro relator |
| `situacao` | string | Status ("OFICIALIZADO", "SIGILOSO", "INVALIDADO") |
| `sumario` | string | Resumo do conteudo do acordao |
| `urlArquivo` | string | URL para download RTF do inteiro teor |
| `urlArquivoPdf` | string | URL para download PDF do inteiro teor |
| `urlAcordao` | string | URL para visualizacao na pesquisa de jurisprudencia |

---

## Endpoint 2: Consultar Atos Normativos

Instrucoes Normativas, Portarias, Decisoes Normativas, Resolucoes e Resolucoes Administrativas do TCU.

| Campo | Valor |
|-------|-------|
| **URL** | `GET https://dados-abertos.apps.tcu.gov.br/api/atonormativo/recupera-atos-normativos` |
| **Auth** | Nenhuma |
| **Status** | INSTAVEL (retornou HTTP 500 em 22/03/2026) |

### Parametros

Nenhum documentado.

### Campos da Resposta (JSON Array)

| Campo | Tipo | Descricao |
|-------|------|-----------|
| `alteradoPelaNorma` | string | Norma que alterou esta |
| `anoAtoNormativo` | string | Ano do ato |
| `colegiado` | string | Colegiado responsavel |
| `dadosRepublicacao` | string | Dados de republicacao |
| `dataSessao` | string | Data da sessao |
| `dataAtualizacao` | string | Data da ultima atualizacao |
| `dataExpedicao` | string | Data de expedicao |
| `dataDOU` | string | Data de publicacao no DOU |
| `ementa` | string | Ementa do ato |
| `urlArquivo` | string | URL do arquivo |
| `normasAlteradasPorEsta` | string | Normas alteradas por este ato |
| `normasRevogadasPorEsta` | string | Normas revogadas por este ato |
| `numeroAta` | string | Numero da ata |
| `numeroAto` | string | Numero do ato |
| `revogadaPelaNorma` | string | Norma que revogou esta |
| `signatario` | string | Signatario |
| `situacao` | string | Vigente/Revogada |
| `tipo` | string | Tipo (Portaria, Resolucao, etc.) |
| `tipoBTCU` | string | Tipo no Boletim TCU |
| `titulo` | string | Titulo completo |
| `textoDocumento` | string | Texto completo do documento |

---

## Endpoint 3: Inabilitados para Funcao Publica

Pessoas inabilitadas para exercer cargo em comissao ou funcao de confianca na Administracao Publica.

| Campo | Valor |
|-------|-------|
| **URL (todos)** | `GET https://contas.tcu.gov.br/ords/condenacao/consulta/inabilitados` |
| **URL (por CPF)** | `GET https://contas.tcu.gov.br/ords/condenacao/consulta/inabilitados/{CPF}` |
| **Auth** | Nenhuma |
| **Status** | ATIVO (verificado 22/03/2026, HTTP 200) |
| **Paginacao** | Oracle ORDS (`offset`, `limit`, `hasMore`, `links`) |

### Parametros

| Parametro | Tipo | Obrigatorio | Descricao |
|-----------|------|-------------|-----------|
| `{CPF}` | path string | Nao | CPF (somente numeros) para filtrar pessoa especifica |
| `offset` | query int | Nao | Deslocamento para paginacao (default: 0) |
| `limit` | query int | Nao | Quantidade por pagina (default: 25) |

### Resposta (JSON Object com paginacao ORDS)

```json
{
  "items": [
    {
      "nome": "ABDALA GOMES SANTOS",
      "cpf": "215.805.453-00",
      "processo": "026.615/2020-7",
      "deliberacao": "AC-000738/2022-PL",
      "data_transito_julgado": "2022-07-16T03:00:00Z",
      "data_final": "2027-07-16T03:00:00Z",
      "data_acordao": "2022-04-06T17:30:00Z",
      "uf": "MA",
      "municipio": "SANTA INES"
    }
  ],
  "hasMore": true,
  "limit": 25,
  "offset": 0,
  "count": 25,
  "links": [
    { "rel": "self", "href": "..." },
    { "rel": "first", "href": "..." },
    { "rel": "next", "href": "...?offset=25&limit=25" }
  ]
}
```

### Campos dos Items

| Campo | Tipo | Descricao |
|-------|------|-----------|
| `nome` | string | Nome da pessoa inabilitada |
| `cpf` | string | CPF formatado (XXX.XXX.XXX-XX) |
| `processo` | string | Numero do processo TCU |
| `deliberacao` | string | Codigo da deliberacao (ex: "AC-000738/2022-PL") |
| `data_transito_julgado` | string (ISO 8601) | Data do transito em julgado |
| `data_final` | string (ISO 8601) | Data final da inabilitacao |
| `data_acordao` | string (ISO 8601) | Data do acordao |
| `uf` | string | Estado (sigla) |
| `municipio` | string | Municipio |

---

## Endpoint 4: Licitantes Inidoneos

Empresas/pessoas declaradas inidoneas pelo TCU para participar de licitacoes.

| Campo | Valor |
|-------|-------|
| **URL (todos)** | `GET https://contas.tcu.gov.br/ords/condenacao/consulta/inidoneos` |
| **URL (por CPF/CNPJ)** | `GET https://contas.tcu.gov.br/ords/condenacao/consulta/inidoneos/{CPF_CNPJ}` |
| **Auth** | Nenhuma |
| **Status** | ATIVO (verificado 22/03/2026, HTTP 200) |
| **Paginacao** | Oracle ORDS (`offset`, `limit`, `hasMore`, `links`) |

### Parametros

| Parametro | Tipo | Obrigatorio | Descricao |
|-----------|------|-------------|-----------|
| `{CPF_CNPJ}` | path string | Nao | CPF ou CNPJ (somente numeros) |
| `offset` | query int | Nao | Deslocamento para paginacao (default: 0) |
| `limit` | query int | Nao | Quantidade por pagina (default: 25) |

### Resposta (JSON Object com paginacao ORDS)

```json
{
  "items": [
    {
      "nome": "A. P. B. J. CONSTRUCOES E SERVICOS LTDA",
      "cpf_cnpj": "07.405.573/0001-44",
      "processo": "007.720/2012-2",
      "deliberacao": "AC-002099/2015-PL",
      "data_transito_julgado": "2021-09-30T03:00:00Z",
      "data_final": "2026-09-30T03:00:00Z",
      "data_acordao": "2015-08-19T17:30:00Z",
      "uf": "DF",
      "municipio": null
    }
  ],
  "hasMore": true,
  "limit": 25,
  "offset": 0,
  "count": 25,
  "links": [...]
}
```

### Campos dos Items

| Campo | Tipo | Descricao |
|-------|------|-----------|
| `nome` | string | Nome da empresa/pessoa inidonea |
| `cpf_cnpj` | string | CPF ou CNPJ formatado |
| `processo` | string | Numero do processo TCU |
| `deliberacao` | string | Codigo da deliberacao |
| `data_transito_julgado` | string (ISO 8601) | Data do transito em julgado |
| `data_final` | string (ISO 8601) | Data final da declaracao de inidoneidade |
| `data_acordao` | string (ISO 8601) | Data do acordao |
| `uf` | string | Estado (sigla) |
| `municipio` | string ou null | Municipio |

**NOTA:** O campo e `cpf_cnpj` (nao `cpf` como no endpoint de inabilitados).

---

## Endpoint 5: Certidoes Consolidadas de Pessoa Juridica (APF)

Consulta consolidada de certidoes de multiplos orgaos (TCU, CNJ, Portal da Transparencia) para verificar situacao de pessoa juridica.

| Campo | Valor |
|-------|-------|
| **URL (tipos)** | `GET https://certidoes-apf.apps.tcu.gov.br/api/rest/publico/tipos-certidoes` |
| **URL (consulta)** | `GET https://certidoes-apf.apps.tcu.gov.br/api/rest/publico/certidoes/{cnpj}` |
| **Auth** | Nenhuma |
| **Status** | ATIVO (verificado 22/03/2026, HTTP 200) |

### 5a. Listar Tipos de Certidoes

`GET https://certidoes-apf.apps.tcu.gov.br/api/rest/publico/tipos-certidoes`

```json
[
  { "orgaoEmissor": "TCU", "sigla": "Inidoneos", "descricao": "Licitantes Inidoneos" },
  { "orgaoEmissor": "CNJ", "sigla": "CNIA", "descricao": "Cadastro Nacional de Condenacoes Civeis por Ato de Improbidade Administrativa e Inelegibilidade" },
  { "orgaoEmissor": "Portal da Transparencia", "sigla": "CEIS", "descricao": "Cadastro Nacional de Empresas Inidoneas e Suspensas" },
  { "orgaoEmissor": "Portal da Transparencia", "sigla": "CNEP", "descricao": "Cadastro Nacional de Empresas Punidas" }
]
```

### 5b. Consultar Certidoes por CNPJ

`GET https://certidoes-apf.apps.tcu.gov.br/api/rest/publico/certidoes/{cnpj}?seEmitirPDF=(true|false)`

### Parametros

| Parametro | Tipo | Obrigatorio | Descricao |
|-----------|------|-------------|-----------|
| `{cnpj}` | path long | Sim | CNPJ (somente numeros, sem formatacao) |
| `seEmitirPDF` | query bool | Nao | Se deve gerar PDF com o resultado |

### Resposta (JSON Object)

```json
{
  "razaoSocial": "Banco do Brasil S.A.",
  "nomeFantasia": "BB",
  "cnpj": "00.000.000/0001-91",
  "uf": null,
  "certidoes": [
    {
      "emissor": "TCU",
      "tipo": "Inidoneos",
      "dataHoraEmissao": "22/03/2026 23:14",
      "descricao": "Licitantes Inidoneos",
      "situacao": "NADA_CONSTA",
      "observacao": null,
      "linkConsultaManual": "https://contas.tcu.gov.br/ords/f?p=INABILITADO:INIDONEOS",
      "tempoGeracao": 44
    },
    {
      "emissor": "CNJ",
      "tipo": "CNIA",
      "dataHoraEmissao": "22/03/2026 23:14",
      "descricao": "CNIA - Cadastro Nacional de Condenacoes Civeis...",
      "situacao": "NADA_CONSTA",
      "observacao": null,
      "linkConsultaManual": "http://www.cnj.jus.br/improbidade_adm/consultar_requerido.php",
      "tempoGeracao": 404
    }
  ],
  "certidaoPDF": null,
  "seCnpjEncontradoNaBaseTcu": true,
  "dataHoraGeracaoInMillis": 1774232056458
}
```

### Campos da Resposta

| Campo | Tipo | Descricao |
|-------|------|-----------|
| `razaoSocial` | string | Razao social da empresa |
| `nomeFantasia` | string | Nome fantasia |
| `cnpj` | string | CNPJ formatado |
| `uf` | string ou null | Estado |
| `certidoes` | array | Lista de certidoes consultadas |
| `certidoes[].emissor` | string | Orgao emissor (TCU, CNJ, Portal da Transparencia) |
| `certidoes[].tipo` | string | Tipo da certidao (Inidoneos, CNIA, CEIS, CNEP) |
| `certidoes[].dataHoraEmissao` | string | Data/hora da emissao (DD/MM/AAAA HH:MM) |
| `certidoes[].descricao` | string | Descricao do cadastro consultado |
| `certidoes[].situacao` | string | Situacao ("NADA_CONSTA" ou detalhes da restricao) |
| `certidoes[].observacao` | string ou null | Observacoes adicionais |
| `certidoes[].linkConsultaManual` | string | Link para consulta manual no orgao |
| `certidoes[].tempoGeracao` | int | Tempo de geracao em milissegundos |
| `certidaoPDF` | string ou null | PDF em base64 (se seEmitirPDF=true) |
| `seCnpjEncontradoNaBaseTcu` | bool | Se o CNPJ foi encontrado na base do TCU |
| `dataHoraGeracaoInMillis` | long | Timestamp da geracao em milissegundos |

---

## Endpoint 6: Calculo de Debito

Calculadora publica para atualizar valores de debitos com correcao monetaria (variacao SELIC) e juros.

| Campo | Valor |
|-------|-------|
| **URL** | `POST https://divida.apps.tcu.gov.br/api/publico/calculadora/calcular-saldos-debito` |
| **Auth** | Nenhuma |
| **Content-Type** | application/json |
| **Status** | ATIVO (verificado 22/03/2026, HTTP 200) |

### Request Body

```json
{
  "dataAtualizacao": "22/03/2026",
  "aplicaJuros": true,
  "parcelasDebito": [
    {
      "dataFato": "01/01/2020",
      "indicativoDebitoCredito": "D",
      "valorOriginal": 1000.00
    }
  ]
}
```

### Parametros do Body

| Campo | Tipo | Obrigatorio | Descricao |
|-------|------|-------------|-----------|
| `dataAtualizacao` | string | Sim | Data de atualizacao (DD/MM/AAAA) |
| `aplicaJuros` | bool | Sim | Se deve aplicar juros de mora |
| `parcelasDebito` | array | Sim | Lista de parcelas do debito |
| `parcelasDebito[].dataFato` | string | Sim | Data do fato gerador (DD/MM/AAAA) |
| `parcelasDebito[].indicativoDebitoCredito` | string | Sim | "D" para debito, "C" para credito |
| `parcelasDebito[].valorOriginal` | float | Sim | Valor original da parcela |

### Resposta (JSON Object)

```json
{
  "data": "22/03/2026",
  "saldoDebito": 1000.0,
  "saldoVariacaoSelic": 577.38,
  "saldoJuros": 0.0,
  "saldoTotal": 1577.38
}
```

### Campos da Resposta

| Campo | Tipo | Descricao |
|-------|------|-----------|
| `data` | string | Data da atualizacao (DD/MM/AAAA) |
| `saldoDebito` | float | Valor original do debito |
| `saldoVariacaoSelic` | float | Correcao monetaria (variacao SELIC) |
| `saldoJuros` | float | Juros de mora (se aplicaJuros=true) |
| `saldoTotal` | float | Valor total atualizado |

---

## Endpoint 7: Solicitacoes do Congresso Nacional (SCN)

Pedidos e solicitacoes de informacao do Congresso Nacional ao TCU.

| Campo | Valor |
|-------|-------|
| **URL (todos)** | `GET https://contas.tcu.gov.br/ords/api/publica/scn/pedidos_congresso` |
| **URL (por processo)** | `GET https://contas.tcu.gov.br/ords/api/publica/scn/pedidos_congresso/{numero_processo}` |
| **Auth** | Nenhuma |
| **Status** | ATIVO (verificado 22/03/2026, HTTP 200) |
| **Paginacao** | Via campo `next` com `$ref` para proxima pagina (`?page=N`) |

### Parametros

| Parametro | Tipo | Obrigatorio | Descricao |
|-----------|------|-------------|-----------|
| `{numero_processo}` | path string | Nao | Numero do processo TCU para filtrar |
| `page` | query int | Nao | Pagina dos resultados |

### Resposta (JSON Object)

```json
{
  "items": [
    {
      "tipo": "REQ",
      "numero": 4,
      "data_aprovacao": "2026-02-19T03:00:00Z",
      "assunto": "Nos termos do art. 71, inciso IV...",
      "autor": "Dr. Hiran",
      "processo_scn": "004.808/2026-6",
      "link_proposicao": "https://www25.senado.leg.br/web/atividade/materias/-/materia/172700",
      "xml_proposicao": "https://legis.senado.leg.br/dadosabertos/materia/pesquisa/lista?..."
    }
  ],
  "first": { "$ref": "..." },
  "next": { "$ref": "http://contas.tcu.gov.br/ords/api/publica/scn/pedidos_congresso?page=1" }
}
```

### Campos dos Items

| Campo | Tipo | Descricao |
|-------|------|-----------|
| `tipo` | string | Tipo da solicitacao ("REQ" = requerimento, "SIT" = solicitacao de informacao) |
| `numero` | int | Numero da solicitacao |
| `data_aprovacao` | string (ISO 8601) | Data de aprovacao |
| `assunto` | string | Descricao do assunto/pedido |
| `autor` | string ou null | Nome do autor (parlamentar) |
| `processo_scn` | string | Numero do processo no TCU |
| `link_proposicao` | string | Link para a proposicao no Senado ou Camara |
| `xml_proposicao` | string | Link para o XML da proposicao nos dados abertos |

---

## Endpoint 8: Pautas das Sessoes

Pautas das sessoes de julgamento dos colegiados do TCU.

| Campo | Valor |
|-------|-------|
| **URL** | `GET https://dados-abertos.apps.tcu.gov.br/api/pautassessao` |
| **Auth** | Nenhuma |
| **Status** | TIMEOUT (nao respondeu em 120s em 22/03/2026 -- pode ser instavel) |

### Parametros

Nenhum documentado.

### Campos da Resposta (JSON Array)

| Campo | Tipo | Descricao |
|-------|------|-----------|
| `dataSessao` | string | Data da sessao |
| `naturezaProcesso` | string | Natureza do processo |
| `nomeColegiado` | string | Nome do colegiado |
| `nomeRelator` | string | Nome do relator |
| `numeroProcesso` | string | Numero do processo |
| `siglaColegiado` | string | Sigla do colegiado |
| `siglaRelator` | string | Sigla do relator |
| `tipoProcesso` | string | Tipo do processo |

---

## Endpoint 9: Termos Contratuais do TCU

Contratos, aditamentos e termos contratuais firmados pelo proprio TCU.

| Campo | Valor |
|-------|-------|
| **URL** | `GET https://contas.tcu.gov.br/contrata2RS/api/publico/termos-contratuais` |
| **Auth** | Nenhuma |
| **Status** | ATIVO (verificado 22/03/2026, HTTP 200) |
| **Paginacao** | Nenhuma (retorna todos — 3859 registros em 22/03/2026) |

### Parametros

Nenhum documentado.

### Resposta (JSON Array)

```json
[
  {
    "codigoTipoContratacao": 9,
    "tipoContratacao": "CONTRATACAO POR NOTA DE EMPENHO",
    "numero": 3,
    "ano": 2025,
    "unidadeGestora": "SEC-RJ",
    "codUnidadeGestora": 199180,
    "nomeFornecedor": "LABORATORIO RICHET...",
    "cnpjFornecedor": "31887136000199",
    "objeto": "CONTRATACAO DE LABORATORIO ESPECIALIZADO...",
    "valorInicial": 5271.82,
    "dataAssinatura": "2025-10-20T00:00:00-0300",
    "dataInicioVigencia": "2025-10-28T00:00:00-0300",
    "dataTerminoVigencia": "2025-12-31T00:00:00-0300",
    "dataPublicacao": "2025-10-29T00:00:00-0300",
    "numeroProcesso": "017.866/2025-1",
    "modalidadeLicitacao": "DISPENSA DE LICITACAO",
    "numeroAditamentos": 0,
    "valorAtualizado": 5271.82,
    "dataTerminoVigenciaSegundoAditamentos": "2025-12-31T00:00:00-0300",
    "codigo": 32783,
    "codigoModalidadeLicitacao": 48,
    "unidadesFiscalizadoras": [
      {
        "codigo": 300046,
        "sigla": "SEC-RJ",
        "nome": "Secretaria do TCU no Estado do Rio de Janeiro"
      }
    ]
  }
]
```

### Campos da Resposta

| Campo | Tipo | Descricao |
|-------|------|-----------|
| `codigoTipoContratacao` | int | Codigo do tipo de contratacao |
| `tipoContratacao` | string | Descricao do tipo (ex: "CONTRATACAO POR NOTA DE EMPENHO") |
| `numero` | int | Numero do contrato |
| `ano` | int | Ano do contrato |
| `unidadeGestora` | string | Sigla da unidade gestora |
| `codUnidadeGestora` | int | Codigo da unidade gestora |
| `nomeFornecedor` | string | Nome do fornecedor |
| `cnpjFornecedor` | string | CNPJ sem formatacao |
| `objeto` | string | Descricao do objeto contratado |
| `valorInicial` | float | Valor inicial do contrato |
| `dataAssinatura` | string (ISO 8601) | Data de assinatura |
| `dataInicioVigencia` | string (ISO 8601) | Data de inicio da vigencia |
| `dataTerminoVigencia` | string (ISO 8601) | Data de termino da vigencia |
| `dataPublicacao` | string (ISO 8601) | Data de publicacao |
| `numeroProcesso` | string | Numero do processo TCU |
| `modalidadeLicitacao` | string | Modalidade da licitacao |
| `numeroAditamentos` | int | Quantidade de aditamentos |
| `valorAtualizado` | float | Valor atualizado com aditamentos |
| `dataTerminoVigenciaSegundoAditamentos` | string (ISO 8601) | Data de termino segundo aditamentos |
| `codigo` | int | Codigo interno |
| `codigoModalidadeLicitacao` | int | Codigo da modalidade |
| `unidadesFiscalizadoras` | array | Unidades fiscalizadoras |
| `unidadesFiscalizadoras[].codigo` | int | Codigo da unidade |
| `unidadesFiscalizadoras[].sigla` | string | Sigla da unidade |
| `unidadesFiscalizadoras[].nome` | string | Nome completo da unidade |

---

## Endpoint 10: CADIRREG (Cadastro de Responsaveis com Contas Irregulares)

Consulta de pessoas com contas julgadas irregulares pelo TCU.

| Campo | Valor |
|-------|-------|
| **URL** | `GET https://dados-abertos.apps.tcu.gov.br/api/recuperapessoacadirreg/{cpf}` |
| **Auth** | Nenhuma |
| **Status** | ATIVO (verificado 22/03/2026, HTTP 200 -- retorna `[]` para CPF inexistente) |

### Parametros

| Parametro | Tipo | Obrigatorio | Descricao |
|-----------|------|-------------|-----------|
| `{cpf}` | path string | Sim | CPF (somente numeros) |

### Campos da Resposta (JSON Array)

| Campo | Tipo | Descricao |
|-------|------|-----------|
| `anoProcesso` | string | Ano do processo |
| `codigoOrigemRecurso` | string | Codigo da origem do recurso |
| `codigoProcesso` | string | Codigo do processo |
| `codigoSecex` | string | Codigo da Secex responsavel |
| `deliberacao` | array | Deliberacoes associadas |
| `dvProcesso` | string | Digito verificador do processo |
| `julgamento` | string | Informacoes do julgamento |
| `nomeResponsavel` | string | Nome do responsavel |
| `numCPF` | string | CPF do responsavel |
| `numProcesso` | string | Numero do processo |
| `seDetentorCargoFuncaoPublica` | string | Se e detentor de cargo/funcao publica |
| `seFalecido` | string | Se falecido |
| `situacao` | array | Situacoes do processo |
| `unidadeTecnicaProcesso` | string | Unidade tecnica do processo |

---

## Dados para Download (CSV)

Alem das APIs REST, o TCU disponibiliza bases completas em CSV:

### Jurisprudencia (https://sites.tcu.gov.br/dados-abertos/jurisprudencia/)

5 bases de dados, todas em CSV, atualizadas periodicamente:

1. **Acordaos Completos** — Organizados por ano. Campos: KEY, TIPO, TITULO, NUMACORDAO, ANOACORDAO, NUMATA, COLEGIADO, DATASESSAO, RELATOR, SITUACAO, PROC, ACORDAOSRELACIONADOS, TIPOPROCESSO, INTERESSADOS, ENTIDADE, RELATORDELIBERACAORECORRIDA, MINISTROREVISOR, MINISTROAUTORVOTOVENCEDOR, REPRESENTANTEMP, UNIDADETECNICA, ADVOGADO, ASSUNTO, SUMARIO, ACORDAO, DECISAO, QUORUM, MINISTROALEGOUIMPEDIMENTOSESSAO, RECURSOS, RELATORIO, VOTO, DECLARACAOVOTO, VOTOCOMPLEMENTAR, VOTOMINISTROREVISOR (32 campos)

2. **Jurisprudencia Selecionada** — Campos: KEY, NUMACORDAO, ANOACORDAO, COLEGIADO, AREA, TEMA, SUBTEMA, ENUNCIADO, EXCERTO, NUMSUMULA, DATASESSAOFORMATADA, AUTORTESE, FUNCAOAUTORTESE, TIPOPROCESSO, TIPORECURSO, INDEXACAO, INDEXADORESCONSOLIDADOS, PARAGRAFOLC, REFERENCIALEGAL, PUBLICACAOAPRESENTACAO, PARADIGMATICO (21 campos)

3. **Sumulas** — Campos: KEY, NUMERO, ENUNCIADO, TIPOPROCESSO, AREA, TEMA, SUBTEMA, APROVACAO, NUMAPROVACAO, ANOAPROVACAO, COLEGIADO, FUNCAOAUTORTESE, AUTORTESE, INDEXACAO, VIGENTE, DATASESSAOFORMATADA, EXCERTO, REFERENCIALEGAL, INDEXADORESCONSOLIDADOS, PUBLICACAO (20 campos)

4. **Boletim de Jurisprudencia / Pessoal** — Campos: KEY, ENUNCIADO, REFERENCIA, TEXTOACORDAO, TITULO, NUMERO (5-6 campos)

5. **Informativo de Licitacoes e Contratos** — Campos: KEY, COLEGIADO, TEXTOACORDAO, ENUNCIADO, NUMERO, TEXTOINFO, TITULO (7 campos)

### Normas (https://sites.tcu.gov.br/dados-abertos/normas/)

Base unica em CSV. Campos: KEY, UNIDADEBASICAAUTORA, ORIGEM, NUMNORMA, ANONORMA, TIPONORMA, NUMEROPROCESSO, NUMEROPROCESSOFORMATADO, TITULO, ASSUNTO, TEXTONORMA, DATAINICIOVIGENCIA, DATAFIMVIGENCIA, SITUACAO, LINKBTCU, TEXTOANEXO, ARQUIVONORMA, PAGINABTCU, TEMA, TAGSVCE, NORMARELACIONADA, NUMDOU, NUMSECAODOU, NUMPAGINADOU, DATADOU, INFOSGERAIS (26 campos)

### Inidoneos e Inabilitados (https://sites.tcu.gov.br/dados-abertos/inidoneos-irregulares)

2 listas em CSV com campos identicos: NOME, CPF, PROCESSO, DELIBERACAO, DATA TRANSITO JULGADO, DATA FINAL, DATA ACORDAO, UF, MUNICIPIO (9 campos)

---

## Resumo de Viabilidade para mcp-brasil

### Endpoints Recomendados (ATIVOS e verificados)

| # | Endpoint | Prioridade | Justificativa |
|---|----------|------------|---------------|
| 1 | Acordaos | ALTA | Dados de decisoes do TCU -- essencial para transparencia |
| 2 | Inabilitados | ALTA | Consulta de pessoas inabilitadas para funcao publica |
| 3 | Inidoneos | ALTA | Consulta de licitantes inidoneos |
| 4 | Certidoes APF | ALTA | Consulta consolidada de 4 cadastros (TCU + CNJ + CGU) |
| 5 | Pedidos do Congresso | MEDIA | Solicitacoes do Congresso ao TCU |
| 6 | Calculo de Debito | MEDIA | Ferramenta util para calculo de dividas |
| 7 | Termos Contratuais | MEDIA | Transparencia dos proprios contratos do TCU |
| 8 | CADIRREG | BAIXA | Contas irregulares -- requer CPF especifico |

### Endpoints Instaveis

| # | Endpoint | Status | Nota |
|---|----------|--------|------|
| 9 | Atos Normativos | HTTP 500 | Instavel em 22/03/2026 |
| 10 | Pautas das Sessoes | TIMEOUT | Nao respondeu em 120s |

### Pontos de Atencao

1. **Nenhuma autenticacao** necessaria para nenhum endpoint
2. **Sem rate limits documentados** -- recomendar paginacao e cache
3. **Formatos de data inconsistentes**: DD/MM/AAAA (acordaos, debito), ISO 8601 (ORDS endpoints, contratos), DD/MM/AAAA HH:MM (certidoes)
4. **Paginacao varia por dominio**: ORDS usa `offset`/`limit`; acordaos usa `inicio`/`quantidade`; SCN usa `page`; contratos nao pagina
5. **Endpoint de licitacoes do TCU** (portal.tcu.gov.br/lumis) retorna 404 -- provavelmente descontinuado
6. **Endpoint de atos normativos** instavel (HTTP 500)
7. **Campo CPF vs CPF_CNPJ**: inabilitados usa `cpf`, inidoneos usa `cpf_cnpj`
