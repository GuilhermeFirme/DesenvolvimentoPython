salario = float(input('Qual seu salário: '))
print('Para salários superiores R$1.250,00 Aumento de 10% \n'
      'Salários inferiores a R$1.250,00 Aumento de 15%')

if salario > 1250:
    aumento = salario * 0.1
    salario = aumento + salario
    print('Seu aumento de 10% foi de: R${}'.format(aumento))
    print('Seu aumento foi de 10% Seu salário agora é: {0}'.format(salario))
if salario <= 1250:
    aumento = salario * 0.15
    salario = aumento + salario
    print('Seu aumento de 15% foi de: R${}'.format(aumento))
    print('Seu aumento foi de 15% Seu salário agora é: {0}'.format(salario))
