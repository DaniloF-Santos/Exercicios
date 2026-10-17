from datetime import datetime
from os import system
system('cls')

#  Iniciando a classe serviço 
class servico: 
    # contrutor/inicialize da classe 
    def __init__(self, descricao, preco):
        self.descricao = descricao
        self.preco = preco 
        self.data = datetime.today().strftime('%d/%m/%Y')
        self.hora = datetime.now().strftime('%H:%M:%S')
    # metodo para exibir os dados do serviço 
    def exibir_dados(self):
        print(f'data: {self.data}')
        print(f'hora: {self.hora}')
        print(f'descricao: {self.descricao}')
        print(f'preco: R${self.preco:.2f}')
    
    # método para salvar dados em TXT
    def salvar_historico(self):

        # abre o arquivo em modo de escrita (append) para adicionar novos registros
        # utf-8 é usado para suportar caracteres especiais

        with open('historico_servico.txt','a', encoding='utf-8') as f:
            f.write(f'Data: {self.data}\n')
            f.write(f'Hora: {self.hora}\n')
            f.write(f'Descrição: {self.descricao}\n')
            f.write(f'Preço: R$ {self.preco:.2f}\n')
            f.write('-' * 40 + '\n')

# iniciando o codigo principal 
print(' == CADASTRO DE SERVIÇOS == ')

continuar = 'x'

while continuar.upper() != 'x':


    descricao = input('informe a descrição do serviço: ')
    preco = float(input('informe o preço do serviço: '))

    try:
        preco = float(preco)

    except ValueError:
        print('Preço inválido. Por favor, insira um número válido.')
        continue

    system('cls')


    # criando uma instancia da classe serviço
    servico = servico(descricao, preco)

    # exibir dados do serviço 
    servico.exibir_dados() 

    servico.salvar_historico()
    print('-' * 40)

    continuar = input('tecle "enter" para continuar ou "x" para sair: ')
    system('cls')
