from os import system
import random # random = utilizado para gerar números aleatórios
system('cls')


continua = 'S'

while continua == 'S':
    

    computador = random.randint(0,2)
    jogador = int(input(''' Opções:
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA
    Escolha uma opção: '''))
    system ('cls')

    if jogador >=0 and jogador <=2:
        pecas = ('Pedra', 'Papel', 'Tesoura')
        print(f'Computador escolheu {pecas[computador]}')
        print(f'Você escolheu {pecas[jogador]}')
        

        tabela = ((0 , 1 , -1) , (-1 , 0 , 1) , (1 , -1 , 0))
        jogada = tabela[computador][jogador]


        if jogador == -1:
            print('Você perdeu!')
        elif jogada == 0:
            print('Empate!')
        else:
            print('Você venceu a MÁQUINA!!!')


    else:
        print('Jogador escolheu uma opção INVÁLIDA!')
    continua = input('Digite [S] para jogar novamente: ').upper()
