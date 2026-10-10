from os import system
system('cls')
import time

numero = int(input('Informe um número maior que 0'))

# Verifica se o número é positivo
if numero <= 0:
    print('Número Inválido!')
else:
# Iniciando Laço For
    for i in range(numero):
        print(f'Valor da Variável i: {i}')
        time.sleep(2)
