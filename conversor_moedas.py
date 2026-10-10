# converter moedas REAL / DÓLAR / EUROS
from os import system
system('cls')

real = float(input('Digite o valor em Reais (R$): '))
print('Escolha a moeda para conversão: ')
print('1 - Dolar (US$)')
print('2 - Euro (€)')
opcao = int(input('Opção: '))

# :.2f = formatação para duas casas decimais
if opcao == 1:
    dolar = real / 5.13
    print('R$ {:.2f} equivale a US$ {:.2f}' . format(real, dolar))
elif opcao == 2:
    euro = real / 5.95
    print('R$ {:.2f} equivale a € {:.2f}' . format(real, euro))
else:
    print('Opção Inválida!')


