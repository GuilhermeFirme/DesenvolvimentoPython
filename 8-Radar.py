import locale

v = float(input('Qual velocidade: '))
if v > 80:
    multa = v - 80
    print('Você foi multado! '
          'Você ultrapassou o limite de velocidade 80Km/h\n'
          'Valor da sua multa é: R$ {:.2f}'.format(multa * 7))
else:
    print('Velocidade regular!')