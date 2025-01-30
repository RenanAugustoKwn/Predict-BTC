import pandas as pd
import streamlit as st
from sklearn import linear_model

df = pd.read_csv("PlanilhaBTC.CSV", sep=";")

modelo = linear_model.LinearRegression()
x = df[["ANO"]]
y = df[["DOLAR"]]

st.title("Prevendo o valor do Bitcoin")
st.divider()
ano = st.number_input("Digite o ano do Bitcoin: ")
