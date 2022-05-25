import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = 'xxxxxxx'
# Your Auth Token from twilio.com/console
auth_token = 'xxxxxxx'
client = Client(account_sid, auth_token)

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

# Para cada arquivo:
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')

    # Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes}, o vendedor {vendedor}, bateu a meta e realizou {vendas} Vendas !!! ')
    # Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor
        message = client.messages.create(
            to="+5513487274858",
            from_="+19804002866",
            body=f'No mês de {mes} o vendedor {vendedor}, bateu a meta e realizou {vendas} Vendas !!! ')
        print('SMS enviado com sucesso !', message.sid)








