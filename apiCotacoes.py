import requests


def buscarCotacoes():
    return requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL").json()


cotacoes = buscarCotacoes()

cotacaoDolar = cotacoes['USDBRL']['bid']
cotacaoEuro = cotacoes['EURBRL']['bid']
cotacaoBitcoin = cotacoes['BTCBRL']['bid']

print(f'Cotacoes: {cotacoes}')

print(f'\nDolar: {cotacaoDolar}')
print(f'\nEuro: {cotacaoEuro}')
print(f'\nBitcoin: {cotacaoBitcoin}')
