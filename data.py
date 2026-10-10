from datetime import datetime
from os import system
system('cls')

# Pegar data atual do sistema
data_atual = datetime.now()
print(f'Data atual: {data_atual}')

# Criar data (Ano, Mês, Dia, Hora, Minuto, Segundo, Microsegundo)
data_criada = datetime(2024, 9, 15, 10, 28, 11, 123456)
print(f'Data criada: {data_criada}')

# Pedir data ao usuário
data_usuario = input('Digite uma data no formato dd/mm/aaaa: ')
print(f'Sua data é: {data_usuario}')
print(type(data_usuario))

# Converter string para data
data_convertida = datetime.strptime(data_usuario, '%d/%m/%Y')
print(type(data_convertida))

