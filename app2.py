import pandas as pd
import streamlit as st
import yfinance as yf
from sklearn import linear_model


# Funcoes e Coleta de Daddos
@st.cache_data
def carregar_dados(empresa):
    texto_tikers = " ".join(empresa)
    dados_acao = yf.Tickers(texto_tikers)
    cotacoes_acao = dados_acao.history(
        period="1d", start="2010-01-01", end="2024-12-31"
    )
    cotacoes_acao = cotacoes_acao["Close"]
    return cotacoes_acao


acoes = ["ITUB4.SA", "PETR4.SA", "MGLU3.SA"]
dados = carregar_dados(acoes)


st.write(""" # APP Preco de Acoes e Predicao do preco do Bitcoin para o futuro""")
st.sidebar.header("Filtros")

## Filtros dos dados
lista_acoes = st.sidebar.multiselect("Escolha as acoes para visualizar", dados.columns)

if lista_acoes:
    dados = dados[lista_acoes]
    if len(lista_acoes) == 1:
        acao_unica = lista_acoes[0]
        dados = dados.rename(columns={acao_unica: "Close"})


data_inicial = dados.index.min().to_pydatetime()
data_final = dados.index.max().to_pydatetime()
intervalo_data = st.sidebar.slider(
    "Selecione o período",
    min_value=data_inicial,
    max_value=data_final,
    value=(data_inicial, data_final),
)

## Data seleionada pelo Usuario
dados = dados.loc[intervalo_data[0] : intervalo_data[1]]
st.write(""" # Gráfico com as acoes escolhidas""")

if lista_acoes:
    st.line_chart(dados)
