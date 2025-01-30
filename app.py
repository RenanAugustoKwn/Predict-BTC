import pandas as pd
import streamlit as st
from sklearn import linear_model

# Carregar dados
df = pd.read_csv("PlanilhaBTC.CSV", sep=";")

# Criar e treinar o modelo
modelo = linear_model.LinearRegression()
x = df[["ANO"]].values  # Garantir que seja um array 2D
y = df[["DOLAR"]].values  # Garantir que seja um array 2D

modelo.fit(x, y)

# Interface do Streamlit
st.title("Prevendo o valor do Bitcoin")
st.divider()

# Input do usuário
ano = st.number_input("Digite o ano do Bitcoin:", min_value=2000, max_value=2100, step=1, format="%d")

# Fazer previsão quando o usuário inserir um ano
if ano:
    ano_array = [[ano]]  # Corrigido: Transformando em um array 2D
    predict_dolar = modelo.predict(ano_array)[0][0]  # Obtendo o valor escalar
    st.write(f"O Valor do Bitcoin no ano de {ano} será de **R${predict_dolar:.2f}**")
