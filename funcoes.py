from os import system
system('cls')

def Somar(a,b):
    try:
        print(f'Somar: {a}+{b}={a+b}')
    except:
        print('Erro')


def Subtrair(a,b):
    try:
        print(f'Subtrair: {a}-{b}={a-b}')
    except:
            print('Erro')


def Multiplicar(a,b):
    try:
        print(f'Multiplicar: {a}X{b}={a*b}')
    except:
            print('Erro')


def Dividir(a,b):
    try:
        print(f'Dividir: {a}/{b}={a/b}')
    except ZeroDivisionError as erro:
          print('Impossível Divisão por Zero!')
    except:
        print('Erro Desconhecido')

opcao = ''

while opcao.upper() != 'X':
    system('cls')


    num1 = float(input('Informe o primeiro número: '))
    num2 = float(input('Infome o segundo número: '))

    opcao = int(input('''
    Opções:
    [1] - Somar
    [2] - Subtrair
    [3] - Multiplicar
    [4] - Dividir
    Escolha uma opção: '''))

    if opcao == 1:
            Somar(num1, num2)
    elif opcao == 2:
            Subtrair(num1, num2)
    elif opcao == 3:
            Multiplicar(num1, num2)
    elif opcao == 4:
            Dividir(num1, num2)
    else:
            print('Opção Inválida')

    opcao = input('Aperte X para finalizar ou Enter para outro cálculo: ')
