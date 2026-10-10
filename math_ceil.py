from os import system
import math

system("cls")

# Uma loja precisa armazenar seus produtos em caixas.
# Cada caixa pode conter no máximo 10 produtos.

num_produtos = int(input('Informe o número de produtos: '))
produtos_caixa = int(input('Informe a qtde de produtos por caixa: '))

qtde_caixas = math.ceil(num_produtos / produtos_caixa)
print(f'Caixas necessárias: {qtde_caixas}')