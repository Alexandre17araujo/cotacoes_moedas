import requests
import json
import matplotlib.pyplot as plt

## Pegar a cotação atual de todas as moedas

#link = https://docs.awesomeapi.com.br/api-de-moedas

cotacoes_dolar = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/15')
cotacoes_dic_dolar = cotacoes_dolar.json()

cotacoes_euro = requests.get('https://economia.awesomeapi.com.br/json/daily/EUR-BRL')
cotacoes_dic_euro = cotacoes_euro.json()

cotacoes_bitcoin = requests.get('https://economia.awesomeapi.com.br/json/daily/BTC-BRL')
cotacoes_dic_bitcoin = cotacoes_bitcoin.json()

## Qual foi a útima cotação do Dólar, do Euro e do BitCoin?

print('\nCotação DOLAR:   {}'.format(cotacoes_dic_dolar[0]['bid']))
print('Cotação EURO:    {}'.format(cotacoes_dic_euro[0]['bid']))
print('Cotação BitCoin: {}\n'.format(cotacoes_dic_bitcoin[0]['bid']))

## Pegar cotações dos últimos 30 dias Dolar

dolar_30_dias = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/30')
dolar_dic_30_dias = dolar_30_dias.json()
lista_cotacoes_dolar = [float(item['bid']) for item in dolar_dic_30_dias] # Converter de texto para float

## Pegar cotações do BitCoin Jan/24 a Out/24

# Vamos pegar 200 contações entre 01/01/2024 até 31/10/2024
# Por algum motivo a API só retorna 90 ultimos resultados.

cotacoes_bitcoin_jan_out = requests.get('https://economia.awesomeapi.com.br/USD-BRL/90?start_date=20240101&end_date=20241031')
cotacoes_dic_bitcoin_jan_out = cotacoes_bitcoin_jan_out.json()
#print(len(cotacoes_dic_bitcoin_jan_out))
#print(cotacoes_dic_bitcoin_jan_out)

lista_cotacoes_btc = [float(item['bid']) for item in cotacoes_dic_bitcoin_jan_out]
lista_cotacoes_btc.reverse()
#print(lista_cotacoes_btc)
#print(len(cotacoes_dic_bitcoin_jan_out))

## Gráficos com as cotações do BitCoin

plt.figure(figsize=(15, 5))
plt.plot(lista_cotacoes_btc)
plt.show()