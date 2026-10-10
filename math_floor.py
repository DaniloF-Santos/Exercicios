from os import system
import math

system("cls")
# Um caminhão transporta ??? tonelas de carga.
# Quantas viagens ele precisa fazer somente com capacidade máxima

capacidade_total = int(input('Carga total (em toneladas): '))
carga = float(input('Carga para viagem (em toneladas): '))

qtde_viagens = math.floor(carga / capacidade_total)
carga_restante = carga - (capacidade_total * qtde_viagens)

print(f'Qtde de viagens carga máxima: {qtde_viagens}')
print(f'Carga restante: {carga_restante:.2f}')