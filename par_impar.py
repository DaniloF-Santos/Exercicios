from os import system
system('cls')

numero = int(input('Digite seu número: '))
# porcentagem em cálculo, ele faz a divisão e retorna o RESTO do cálculo
resto = numero % 2
# == para comparar valores IGUAIS
# != para comparar valores DIFERENTES
# < para comparar valores MENORES
# <= para comparar valores MENORES ou IGUAIS
# > para comparar valores MAIORES
# >= para comparar valores MAIORES ou IGUAIS

if resto == 0:
    print('O número {} é PAR!' . format(numero))
else:
    print('O número {} é ÍMPAR!' . format(numero))