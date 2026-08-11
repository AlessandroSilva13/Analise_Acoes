import pandas as pd
import yfinance as yf
import numpy as np
import openpyxl as op
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

data_fim = datetime.today().strftime('%Y-%m-%d')
data_inicio = (datetime.today() - timedelta(days=365)).strftime('%Y-%m-%d')

acoes = yf.download(
    ['PETR4.SA',
    'VALE3.SA',
    'ITUB4.SA',
    'WEGE3.SA',
    '^BVSP'],
    start=data_inicio,
    end=data_fim
)

df_acoes = acoes

df_close = df_acoes['Close']

df_retornos = (df_close.pct_change())

retorno_acumulado = (1 + df_retornos).cumprod() -1

df_acumulado = retorno_acumulado

matriz_correlação = df_retornos.corr()

retorno_anual = df_retornos.mean() * 252

risco_anual = df_retornos.std() * np.sqrt(252)

taxa_livre_de_risco = 0.14

sharpe = (retorno_anual - taxa_livre_de_risco)/ risco_anual

with pd.ExcelWriter('analise_acoes.xlsx') as writer:
    df_close.to_excel(writer, sheet_name='Precos')
    df_retornos.to_excel(writer, sheet_name='Retornos_Diarios')
    df_acumulado.to_excel(writer, sheet_name='Retorno_Acumulado')
    matriz_correlação.to_excel(writer, sheet_name='Correlação')
    sharpe.to_excel(writer, sheet_name ='Indice_Sharpe')

periodo_titulo = f"{datetime.strptime(data_inicio, '%Y-%m-%d').strftime('%b/%Y')} a {datetime.strptime(data_fim, '%Y-%m-%d').strftime('%b/%Y')}"

plt.figure(figsize=(12, 6))

for coluna in df_acumulado.columns:
    plt.plot(df_acumulado.index, df_acumulado[coluna] * 100, label=coluna)

plt.title(f'Retorno Acumulado (%) - {periodo_titulo}')
plt.xlabel('Data')
plt.ylabel('Retorno Acumulado (%)')
plt.legend()
plt.grid(alpha=0.3)
plt.savefig('retorno_acumulado.png', dpi=300, bbox_inches='tight')
plt.show()

plt.figure(figsize= (8, 6))

sns.heatmap(
    matriz_correlação,
    annot=True,
    fmt='.2f',
    cmap='coolwarm',
    vmin=-1, vmax=1
)

plt.title(f'Correlação entre Ativos - {periodo_titulo}')
plt.savefig('correlacao_heatmap.png', dpi=300, bbox_inches='tight')
plt.show()

plt.figure(figsize= (10, 6))
cores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
plt.bar(sharpe.index, sharpe.values, color=cores)
plt.title(f'Indice Sharpe Ratio (%) - {periodo_titulo}')
plt.xlabel('Ações')
plt.ylabel('Sharpe Ratio')
plt.axhline(0, color='black', linewidth=0.8)
plt.savefig('Indice_Sharpe.png', dpi=300, bbox_inches='tight')
plt.show()