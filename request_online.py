from os import system
system('cls')
import requests

print(f'{'ID' :<3} | {'title' :<97} | {'price' :<6}')
print('-' * 112)

# Trazer informações via API da loja FakeStore
produtos = requests.get('https://fakestoreapi.com/products')

# Converter informações para JSON
produtos = produtos.json()
for produto in produtos:
    id = produto['id']
    title = produto['title']
    price = produto['price']

    #Exibir informações em lista
    print(f'{id:<3} | {title:<97} | {price:<6}')
    print('-' * 112)