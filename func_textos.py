from os import system
system('cls')
# Funções para trabalhar com texto
nomecompleto = input('Digite seu nome Completo: ')

# len = lengh - conta o número de caracteres
print('- Função para contar caracteres: ' , len(nomecompleto.strip()))
print('-Função para texto maiúsculo: ' , nomecompleto.upper())
print('-Função para texto minúsculo: ' , nomecompleto.lower())
print('-Função para primeiro maiúsculo: ' , nomecompleto.capitalize())
print('-Função para primeira letra de cada palavra maiúscula: ' , nomecompleto.title())
print('-Função para remover espaços antes e depos do texto: ' , nomecompleto.strip())
espaco = nomecompleto.find(' ')
print('- Primeiro nome: ' , nomecompleto[0:espaco])

# find = encontrar a posição do caractere
# replace = busca e substitui o texto
print('-Remover espaços vazios: ' , nomecompleto.replace(' ' , ''))
print('- Função para contar caracteres sem espaço: ' , len(nomecompleto.replace(' ' , '')))
