# Calcular área de um retângulo
# float =  ponto flutuante, ou seja, aceita casas decimais
base = input('Infome o valor da base: ')
altura = input('Informe o valor da altura: ')

# Valida se os valores informados são números
print('Base é numérico?' , base.isdecimal())
print('Altura é numérico?' , altura.isdecimal())

# Calcula área do quadradp
area_quadrado = float(base)*float(altura)
#print('O resultado do seu cálculo de área com a base' , base , ' e com a altura' , altura , 'é de' , area_quadrado)
print('O valor da área com a base {} e altura {} é de {}' . format(base, altura, area_quadrado))
