# ETL - Extrair, Transforma e Carregar
# 1. Extrair dados de um CSV;
# 2. Trabalhar com as informações do arquivo, retirando a API do processo, e transformar os dados;
# 3. Armazer os dados transformados em outra planilha ou banco de dados ou json etc.

from IPython.display import display
import pandas as pd
import openai

openai_api_key = 'TODO'
openai.api_key = openai_api_key

# chatGPT
def generate_ai_news(tab, psna):
    completion = openai.ChatCompletion.create(
        model= "gpt-4",
        messages=[
            {
                "role": "system", 
                "content": f"Você é responsável pela Segurança Operacional do seguinte Órgão ATS: {psna}, com conhecimento de análise de dados."
            },
            {
                "role": "user", 
                "content": f"Crie recomendações de segurança para o PSNA {psna}, analisando os seguintes dados de ocorrências disponíveis: {tab}."
            }
        ]
    )

    return completion.choices[0].message.content.strip('\"')


tabela = pd.read_excel("colisao_com_aves.xlsx")

# Visualizar a base de dados
display(tabela)
# - Entender quais as informações tão disponíveis
# - Descobrir as cagadas da base de dados
print(tabela.info())

# Tratamento de dados
# - Valores vazios

# deletando as colunas desnecessárias
tabela = tabela.drop(['CLASSE DA OCORRÊNCIA', 'CATEGORIA'], axis=1)
display(tabela)

# deletando as linhas vazias
tabela = tabela.dropna(subset=['EVENTO', 'PSNA'])
print(tabela.info())

tabela['DATAS'] = pd.to_datetime(tabela['DATA']).dt.date
tabela['HORARIOS'] = pd.to_datetime(tabela['DATA']).dt.time

tabela = tabela.drop('DATA', axis=1)

display(tabela)

psna = input("Para qual PSNA gostaria de receber análise com os dados disponíveis de risco aviário? ")

tabela_psna = tabela.query(f"PSNA == '{psna}'")

# Recomendação de segurança do chatGPT
recomendacao = generate_ai_news(tabela_psna.describe().to_string, psna)
print(recomendacao)

# Carregando dados tratados para um arquivo
tabela_psna.to_excel('analíse_psna.xlsx', index=False)