print('\033[4;;46m Bem-vindo !\033[m\n'
      'Qual seu nome?')
corretor = str(input())
print('Olá {}'.format(corretor))
valor = float(input('Digite o valor da casa:'))
salario = float(input('Digite o salario do comprador: '))
anos = int(input('Considerando que cada ano tem 12 Meses. \n'
                 'Digite quantidade de anos para pagar:'))
anos = anos * 12
prestacao = valor / anos
if salario * 0.3 > prestacao:
    print('Para pagar uma casa de R${:.2f} em {} meses, a prestação será de R${:.2f} por Mês.\n'
        'Empréstimo pode ser CONCEDIDO!'.format(valor, anos, prestacao))
else:
    print('Para pagar uma casa de R${:.2f} em {} meses, a prestação será de R${:.2f} por Mês.\n'
          'Empréstimo NEGADO!'.format(valor, anos, prestacao))
    print('A prestação mensal excedeu 30% do salário do Cliente.')


print()
