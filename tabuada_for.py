from os import system
system('cls')

numero = int(input('Informe um número: '))

for i in range(1,11):
    print(f'{numero} x {i} = {numero*i}')
