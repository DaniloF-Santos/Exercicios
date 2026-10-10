from os import system
system('cls')

celsius = float(input('Digite o valor em Celsius (C°): '))
print('Escolha a unidade para conversão: ')
print('1 - Fahrenheit (F°)')
print('2 - Kelvin (K)')
opcao = int(input('Opção: '))
if opcao == 1:
    farenheit = celsius * 1.8 + 32
    print('C° {:.2f} equivale a F° {:.2f}' . format(celsius, farenheit))
elif opcao == 2:
    kelvin = celsius + 273.15
    print('C° {:.2f} equivale a K {:.2f}' . format(celsius, kelvin))
else:
    print('Opção Inválida!')