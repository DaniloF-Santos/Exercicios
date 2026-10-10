from os import system
from datetime import datetime

system('cls')

def calcular_idade(data_nascimento):
    # Data atual
    data_atual = datetime.today()
    data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')

    # calcular idade
    idade = data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day))
    return idade

def idade_dias (data_nascimento):
    # Data atual
    data_atual = datetime.today()
    data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')

    # Calcular idade em dias
    idade_dias = (data_atual - data_nascimento).days
    return idade_dias

# Pedir data nascimento do usuário
data_nascimento = input('Digite sua data de nascimento (dd/mm/aaaa): ')
print(f'Sua idade é: {calcular_idade(data_nascimento)} anos.')
print(f'Você já viveu: {idade_dias(data_nascimento)} dias.')

