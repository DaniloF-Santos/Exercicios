from os import system
system('cls')

salario = input('Digite seu Salário: ')
salario = float(salario.replace(',' , '.'))

if salario <= 1621:
   aliquota = salario * 0.075
   desconto = salario * 0.075
   salario_sem_irpf = salario - desconto
   print('Sua alíquota será de {:.2f}, não terá parcela a reduzir, seu desconto final será {:.2f} e o seu salário sem os descontos do IRPF será {:.2f}' . format(aliquota, desconto, salario_sem_irpf))
elif salario <= 2902.84:
    aliquota = salario * 0.09
    desconto = salario * 0.09 - 24.32
    salario_sem_irpf = salario - desconto
    print('Sua alíquota será de {:.2f}, a parcela a reduzir é 24,32, seu desconto final será {:.2f} e o seu salário sem os descontos do IRPF será {:.2f}' . format(aliquota, desconto, salario_sem_irpf))
elif salario <= 4354.27:
    aliquota = salario * 0.12
    desconto = salario * 0.12 - 111.41
    salario_sem_irpf = salario - desconto
    print('Sua alíquota será de {:.2f}, a parcela a reduzir é 111,41, seu desconto final será {:.2f} e o seu salário sem os descontos do IRPF será {:.2f}' . format(aliquota, desconto, salario_sem_irpf))
elif salario <= 8475.55:
    aliquota = salario * 0.14
    desconto = salario * 0.14 - 198.50
    salario_sem_irpf = salario - desconto
    print('Sua alíquota será de {:.2f}, a parcela a reduzir é 198,50, seu desconto final será {:.2f} e o seu salário sem os descontos do IRPF será {:.2f}' . format(aliquota, desconto, salario_sem_irpf))
elif salario >= 8475.56:
    desconto = salario - 988.07
    salario_sem_irpf = salario - desconto
    print('Não haverá mais uma porcentagem a descontar, o único desconto será o valor fixo de 988,07 e seu desconto final será {:.2f}, o seu salário sem os descontos do IRPF será {:.2f}' . format(desconto, salario_sem_irpf))

salario_liquido = salario - desconto

if salario_liquido <= 2428.80:
    irpf = salario_liquido
    salario_final = salario_liquido - irpf
    print('Não haverá mais uma porcentagem a descontar nem parcela e seu salário final será {:.2f}' . format(salario_final))
elif salario_liquido <= 2826.65:
    aliquota_final = salario_liquido * 0.075
    irpf = salario_liquido * 0.075 - 182.16
    salario_final = salario_liquido - irpf
    print('Sua alíquota final será de {:.2f}, a parcela a reduzir é 182,16 a reduzir e seu salário líquido final será {:.2f}' . format(aliquota_final, salario_final))
elif salario_liquido <= 3751.05:
    aliquota_final = salario_liquido * 0.15
    irpf = salario_liquido * 0.15 - 394.16
    salario_final = salario_liquido - irpf
    print('Sua alíquota final será de {:.2f}, a parcela a reduzir é 394,16 a reduzir e seu salário líquido final será {:.2f}' . format(aliquota_final, salario_final))
elif salario_liquido <= 4664.68:
    aliquota_final = salario_liquido * 0.225
    irpf = salario_liquido * 0.225 - 675.49
    salario_final = salario_liquido - irpf
    print('Sua alíquota final será de {:.2f}, a parcela a reduzir é 675,49 a reduzir e seu salário líquido final será {:.2f}' . format(aliquota_final, salario_final))
elif salario_liquido >= 4664.69:
    aliquota_final = salario_liquido * 0.275
    irpf = salario_liquido * 0.075 - 908.73
    salario_final = salario_liquido - irpf
    print('Sua alíquota final será de {:.2f}, a parcela a reduzir é 908,73 a reduzir e seu salário líquido final será {:.2f}' . format(aliquota_final, salario_final))