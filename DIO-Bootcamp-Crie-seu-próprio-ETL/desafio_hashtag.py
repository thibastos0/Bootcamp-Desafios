from IPython.display import display
import pandas as pd
import plotly.express as px

# 1. Importar a base de dados
tabela = pd.read_csv("ClientesBanco.csv", encoding='latin1')

# display(tabela)
print(tabela.columns)

# 2. Visualizar e tratar base de dados
# 3. Entender a base de dados
# 4. Construir uma análise para identificar o motivo de cancelamento
#Identificar qual o motivo ou os principais motivos dos clientes estarem cancelando o cartão de crédito
# - Valores que estão reconhecidos de forma errada
# tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")


# deletando as colunas vazias ou desnecessárias
# tabela = tabela.dropna(how="all", axis=1)
tabela = tabela.drop("CLIENTNUM", axis=1)
# display(tabela)
# display(tabela.info())

tabela = tabela.dropna()
display(tabela.info())

display(tabela['Idade'].describe().round(1))

display(tabela['Categoria'].describe())

qtde_categoria = tabela['Categoria'].value_counts()
display(qtde_categoria)

qtde_categoria_perc = tabela['Categoria'].value_counts(normalize=True).map("{:.1%}".format) # para mostrar em percentual
display(qtde_categoria_perc)
# # print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format)

# for linha in tabela.index: # para percorrer linhas
for coluna in tabela: # para percorrer colunas
    #print(coluna)
    if coluna in ['Categoria', 'Idade', 'Sexo', 'Dependentes', 'Educação', 'Estado Civil', 'Faixa Salarial Anual', 'Limite', 'Limite Consumido', 'Mudanças Transacoes_Q4_Q1']:
        continue
    # para mudar a cor do gráfico , color_discrete_sequence=["blue", "green"]
    grafico = px.histogram(tabela, x=coluna, color='Categoria')
    # grafico.show()

