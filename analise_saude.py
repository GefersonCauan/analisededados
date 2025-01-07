import pandas as pd
import numpy as np

# Carregando os dados
try:
    caminho_csv = './static/dados_saude.csv'
    dados = pd.read_csv(caminho_csv)
    print("Dados carregados com sucesso!")

    # Exibindo os primeiros registros
    print("Primeiros registros do dataset:")
    print(dados.head())

    # Análise simples
    print("\nEstatísticas descritivas:")
    print(dados.describe())

    # Calcular taxa de mortalidade por cidade
    dados['taxa_mortalidade'] = (dados['obitos_covid'] / dados['casos_covid']) * 100
    print("\nTaxa de mortalidade por cidade:")
    print(dados[['cidade', 'taxa_mortalidade']])

    # Salvando os dados analisados em um novo arquivo
    dados.to_csv('./static/dados_saude_analisados.csv', index=False)
    print("\nArquivo 'dados_saude_analisados.csv' salvo com sucesso!")

except FileNotFoundError:
    print(f"Erro: O arquivo '{caminho_csv}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
