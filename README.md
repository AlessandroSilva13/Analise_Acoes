# 📊 Análise de Ações B3 — PETR4, VALE3, ITUB4 e WEGE3

Análise quantitativa do comportamento de quatro ações da B3, comparando retorno, risco, correlação e retorno ajustado ao risco (Sharpe Ratio), com atualização automática para os últimos 12 meses a partir da data de execução.

## 🎯 Objetivo

Simular um cenário real de consultoria de investimentos: responder, com dados, qual ação seria mais adequada para um perfil de investidor **conservador**, e demonstrar como essa resposta muda dependendo da janela de tempo analisada.

**Perguntas respondidas:**
1. Qual ação teve o melhor retorno no período?
2. Qual ação apresenta maior risco (volatilidade)?
3. Existe relação de comportamento entre os ativos?
4. Para uma posição conservadora, qual(is) ativo(s) é(são) mais indicado(s)?

## 🛠️ Stack

- **Python 3.11**
- `yfinance` — coleta de dados históricos (Yahoo Finance)
- `pandas` / `numpy` — manipulação e cálculo
- `matplotlib` / `seaborn` — visualização
- `openpyxl` — exportação para Excel
- `datetime` — cálculo dinâmico do período (sempre os últimos 365 dias)

## 📁 Estrutura do repositório

```
├── analise_acoes.py          # Script principal
├── analise_acoes.xlsx        # Dados exportados (preços, retornos, correlação, Sharpe)
├── retorno_acumulado.png     # Gráfico: evolução do retorno acumulado
├── correlacao_heatmap.png    # Gráfico: matriz de correlação entre ativos
├── Indice_Sharpe.png         # Gráfico: Sharpe Ratio comparado
├── relatorio_final.md        # Relatório estruturado (formato corporativo)
└── README.md
```

## 🔢 Metodologia

| Métrica | Fórmula / Método |
|---|---|
| Período | Dinâmico — últimos 365 dias a partir da execução (`datetime.today() - timedelta(days=365)`) |
| Retorno diário | `df_close.pct_change()` |
| Retorno acumulado | `(1 + retornos).cumprod() - 1` |
| Risco | Desvio padrão dos retornos diários, anualizado (`std() * √252`) |
| Correlação | Correlação de Pearson entre retornos diários (`.corr()`) |
| Sharpe Ratio | `(retorno anualizado − taxa livre de risco) / risco anualizado` |

**Taxa livre de risco:** Selic vigente (14% a.a. em agosto/2026).

## 📈 Resultados — Últimos 12 meses (Ago/2025 a Ago/2026)

| Ativo | Retorno Acumulado | Risco (std anual) | Sharpe Ratio |
|---|---|---|---|
| PETR4 | +49,5% | 25,3% | **1,18** |
| VALE3 | +49,5% | 25,3% | **1,18** |
| WEGE3 | +33,6% | 29,4% | 0,67 |
| Ibovespa | +27,0% | 17,3% | 0,67 |
| ITUB4 | +22,0% | 23,6% | 0,38 |

**Correlação:** ITUB4 é fortemente correlacionada ao Ibovespa (0,86). PETR4 e VALE3, apesar do desempenho idêntico no período, têm correlação praticamente nula entre si (-0,05) — indicando que se movem por fatores independentes.

## 💡 Principal aprendizado do projeto

O ranking de "melhor ação" **não é estático** — depende da janela temporal analisada:

- Numa janela de **5 anos** (2021–2025), **ITUB4** era a recomendação para perfil conservador (menor risco individual entre as ações).
- Nos **últimos 12 meses**, o cenário mudou: **PETR4 e VALE3** lideraram em retorno e em Sharpe Ratio, com diferença de risco pequena o suficiente para justificar reconsiderar a recomendação — reforçado pelo fato de as duas se moverem de forma independente entre si.

Isso reforça um princípio central de análise financeira: **conclusões baseadas em dados históricos têm validade dentro de um período e precisam ser revisitadas**, e a métrica certa depende da pergunta certa (risco individual vs. risco ajustado ao retorno).

## ⚠️ Disclaimer

Este projeto tem fins **educacionais**. Não constitui recomendação de investimento. Dados obtidos via Yahoo Finance; taxa livre de risco aproximada pela Selic vigente.

<<<<<<< HEAD
## 👤 Autor

Alessandro Silva — Projeto desenvolvido como estudo prático de Análise de Dados aplicada a Finanças.
[(https://www.linkedin.com/in/alessandro-m-silva/)] · [https://github.com/AlessandroSilva13]
=======
Projeto desenvolvido como estudo prático de Caso
Análise de Dados aplicada a Finanças.
>>>>>>> 659c80a116d7ba3ed62e1ab481d2201eb6224a7b
