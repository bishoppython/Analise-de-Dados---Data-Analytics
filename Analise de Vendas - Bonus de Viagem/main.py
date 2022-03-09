# 1. Instalar as Bibliotecas:
# Pandas - openpyxl - twillo

# importar as Bibliotecas
import pandas as pd
from twilio.rest import Client

# Gerar SID e Token nesta URL: https://www.twilio.com/docs/libraries/python
# Your Account SID from twilio.com/console
account_sid = "AC54410f8ae1ce1bc9a018b97edd982600"
# Your Auth Token from twilio.com/console
auth_token  = "6046a6917ed5d19fc481b37ddb7ae9b5"

client = Client(account_sid, auth_token)

# Abrir os 6 arquivos em Excel
import pandas as pd

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

#Para Cada Arquivo Validar se existe algum valor na coluna vendas do arquivo e verificar se é maior ou igual a R$ 55.000
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    # any() verifica se tem algum valor dentro da coluna maior que o valor descrito
    if (tabela_vendas['Vendas'] >= 55000).any():                    # se for maior que 55.000 -> Envia um SMS com um Nome, o Mês as vendas do Vendedor
        # loc é um parametro para localizar determinada informação na tabela
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] >= 55000, 'Vendedor'].values[0]
        # No entanto, o loc retorna como uma tabela a informação, para isso inserimos o .values[0], com isto informamos que desejamos apenas o valor e não a tabela
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] >= 55000,'Vendas'].values[0]
        # Vai printar
        print(f'No Mês {mes} alguém bateu a meta. Vendedor {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5581995241524",
            from_="+17657349565",
            body=f'No Mês {mes} alguém bateu a meta. Vendedor {vendedor}, Vendas: {vendas}')
        print(message.sid)

