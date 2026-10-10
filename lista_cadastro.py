from os import system
system("cls")

clientes = []
telefones = []

opcao = ''

while opcao != 'X':
    system("cls")

    nome = input('Digite o nome do cliente: ')
    telefone = input('Digite o telefone do cliente: ')

    clientes.append(nome)
    telefones.append(telefone)

    system('cls')
    print(' -- CADASTRO REALIZADO COM SUCESSO --')

    opcao = input('Aperte X para Finalizar ou Enter para continuar.')

system('cls')

for i in range(len(clientes)):
    print(f'Nome: {clientes[i]} - Telefone: {telefones[i]}')
# Limpa a tela

# Listar registros -> nome: Danilo - Telefone: xxxxxx