import pandas as pd
import streamlit as st
from sklearn import linear_model

# Carregar dados
df = pd.read_csv("PlanilhaBTC.csv", sep=";")

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

csv_ano_array = df[["ANO"]].values

# Verificar se o ano está no DataFrame
if ano in df["ANO"].values:
    predict_dolar = df.loc[df["ANO"] == ano, "DOLAR"].values[0]  # Obtém o valor real do CSV
    st.write(f"O Valor do Bitcoin no ano de {ano} foi de **${predict_dolar:.2f}** (dado real)")

# Fazer previsão quando o usuário inserir um ano
else:
    ano_array = [[ano]]  # Corrigido: Transformando em um array 2D
    predict_dolar = modelo.predict(ano_array)[0][0]  # Obtendo o valor escalar
    if predict_dolar < 0:
        predict_dolar = 0
    st.write(f"O Valor do Bitcoin no ano de {ano} será de **${predict_dolar:.2f}**")
