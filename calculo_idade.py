from os import system 
from datetime import datetime

system('cls')

# pedir data de nascimento do usuario 
data_nascimento = input('digite sua data de nascimento (dd/mm/aaaa): ')
data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')

def calcular_idade(data_nascimento):

    # data atual
        data_atual = datetime.today()

    # calcular idade 
        idade = data_atual.year - data_nascimento.year
        idade_passou = (data_atual.month, data_atual.day) >= (data_nascimento.month, data_nascimento.day)
        print(f'{idade}')
        return idade

print(f'sua idade é: {calcular_idade(data_nascimento)} anos')