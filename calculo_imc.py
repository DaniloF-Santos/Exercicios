from os import system
system('cls')

# Calculadora IMC
altura = input('Digite sua altura em metros: ')

altura = float(altura.replace(',' , '.'))
peso = float(input('Digite o seu peso em quilos: '))

imc = peso / (altura * altura)
print('Seu IMC é: {:.2f}' . format(imc))
# print(f'Seu IMC é: {imc}')
# Esse é outro jeito de usar o format, um jeito um pouco mais curto.
if imc < 18.5:
    print('Abaixo do peso normal')
elif imc < 25:
    print('Peso Ideal')
elif imc < 30:
    print('Excesso de Peso')
elif imc < 35:
    print('Obesidade Classe 1')
elif imc < 40:
    print('Obesidade Classe 2')
elif imc > 40:
    print('Obesidade Classe 3')


    