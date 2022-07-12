from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano
print('Quem nasceu em {}, tem {} anos em {}.'.format(ano, idade, atual))
if idade < 18:
    falta = 18 - idade
    alistamento = falta + atual
    print('Ainda falta {0} anos para seu alistamento\n'
          'Seu alistamento será em {1}.'.format(falta, alistamento))
elif idade > 18:
    passou = idade - 18
    alistamento = atual - passou
    print('Já deveria ter se alistado a {0} anos.\n'
          'Seu alistamento foi em {1}.'.format(passou, alistamento))
else:
    idade = 18
    print('Você tem que se ALISTAR IMEDIATAMENTE!')














