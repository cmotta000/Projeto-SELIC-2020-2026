# 📈 Projeto SELIC 2020–2026

Análise e enriquecimento da Taxa SELIC no período de 2020 a 2026, utilizando **PySpark no Databricks** com entrega final em **Power BI**.

---

## 🎯 Objetivo

Extrair, transformar e enriquecer os dados históricos da Taxa SELIC, criando métricas temporais e indicadores de tendência para suportar análises no Power BI.

---

## 🗂️ Estrutura do Projeto

```
Projeto-SELIC-2020-2026/
│
├── extract/
│   ├── ingestaobcb.py               # Extração da Taxa SELIC via API do BCB e geração do selic.parquet (Pandas)
│   ├── carregamento_databricks.py   # Upload do selic.parquet para o Volume no Databricks
│   ├── volumesdatabricks.py         # Listagem de catálogos e volumes disponíveis
│   └── config.py                    # Configurações de conexão (não sobe credenciais)
│
├── notebook/
│   └── Transformacao_e_Enriquecimento.ipynb  # Notebook principal com PySpark
│
└── selic.csv                        # Dados brutos da Taxa SELIC
```

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Uso |
|---|---|
| Python | Linguagem principal |
| Pandas | Extração da API do BCB e geração do `selic.parquet` |
| PySpark | Transformação e enriquecimento dos dados |
| Databricks | Plataforma de processamento |
| Unity Catalog | Armazenamento em Volume (`main.default.selic`) |
| Power BI | Visualização final (em desenvolvimento) |
| GitHub | Versionamento do código |

---

## ⚙️ Pipeline de Dados

```
[Fonte: BCB]  →  [Pandas: extração e geração do selic.parquet]  →  [Databricks Volume]  →  [PySpark Transform]  →  [Power BI]
```

> O arquivo `selic.parquet` é gerado localmente via **Pandas**, consumindo a API do Banco Central, e em seguida carregado no Volume `main.default.selic` no Databricks via SDK.

---

## 🔄 Transformações Aplicadas

### Extração de Período
- `ano` — Ano da data
- `trimestre` — Trimestre do ano (1 a 4)
- `mes` — Mês do ano (1 a 12)

### Médias por Window Function
- `media_mensal` — Média da SELIC dentro do mês
- `media_trimestre` — Média da SELIC dentro do trimestre
- `media_anual` — Média da SELIC dentro do ano
- `media_movel_30d` — Média móvel dos últimos 30 dias
- `media_movel_90d` — Média móvel dos últimos 90 dias

### Indicadores de Variação
- `valor_anterior` — Taxa do dia anterior (via `lag`)
- `variacao_diaria` — Diferença absoluta dia a dia
- `variacao_pct` — Variação percentual dia a dia

---

## 🚀 Como Executar

### Pré-requisitos
- Conta no Databricks com Unity Catalog habilitado
- Volume criado em `main.default.selic`
- Python 3.11+
- Biblioteca `databricks-sdk`

### Instalação
```bash
pip install databricks-sdk
```

### Configuração
Crie um arquivo `config.py` local (não versionar):
```python
DATABRICKS_HOST  = "SUA_URL_AQUI"
DATABRICKS_TOKEN = "SEU_TOKEN_AQUI"
```

### Upload do arquivo
```bash
python extract/carregamento_databricks.py
```

### Transformação
Execute o notebook `Transformacao_e_Enriquecimento` no Databricks.

---

## 📊 BI (Em desenvolvimento)

A camada de visualização será construída no **Power BI**, consumindo os dados enriquecidos do Databricks, com os seguintes painéis previstos:

- Evolução histórica da Taxa SELIC
- Comparativo por ano e trimestre
- Médias móveis e tendências
- Indicadores de alta e baixa

---

## 🔒 Segurança

- Tokens e credenciais **nunca** são versionados
- Utilize variáveis de ambiente para configurações sensíveis
- O arquivo `config.py` está no `.gitignore`

---

## 👤 Autor

**cmotta000** — [GitHub](https://github.com/cmotta000)

---

## 📄 Fonte dos Dados

Banco Central do Brasil (BCB) — Taxa SELIC diária
