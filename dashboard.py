import streamlit as st
import pandas as pd

# Carregar o dataset
st.title("Dashboard Interativo - Análise de Dados de Saúde")

try:
    dados = pd.read_csv('static/dados_saude.csv')
    
    # Mostrar informações básicas
    st.subheader("Visualização dos Dados")
    st.dataframe(dados)

    # Estatísticas descritivas
    st.subheader("Estatísticas Descritivas")
    st.write(dados.describe())

    # Selecionar coluna para visualização
    colunas = dados.columns.tolist()
    coluna_selecionada = st.selectbox("Selecione uma coluna para visualizar os dados:", colunas)

    st.subheader(f"Dados da coluna: {coluna_selecionada}")
    st.write(dados[coluna_selecionada])

    # Gráficos interativos
    st.subheader("Gráfico Interativo")
    tipo_grafico = st.selectbox("Escolha o tipo de gráfico:", ["Histograma", "Barra", "Linha"])

    if tipo_grafico == "Histograma":
        st.bar_chart(dados[coluna_selecionada])
    elif tipo_grafico == "Barra":
        st.bar_chart(dados[coluna_selecionada].value_counts())
    elif tipo_grafico == "Linha":
        st.line_chart(dados[coluna_selecionada])

except FileNotFoundError:
    st.error("O arquivo 'dados_saude.csv' não foi encontrado. Certifique-se de que ele está na pasta correta.")
except Exception as e:
    st.error(f"Ocorreu um erro inesperado: {e}")
