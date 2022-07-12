p = float(input('Digite seu peso: '))
a = float(input('Digite sua altura: '))
imc = p / pow(a, 2)
if imc < 18.5:
    print('Abaixo do peso!com imc de {:.1f}'.format(imc))

elif imc >=18.5 and imc < 25:
    print('Peso ideal!com imc de {:.1f}'.format(imc))

elif 25 <= imc < 30:
    print('Acima do peso!com imc de {:.1f}'.format(imc))

elif 30 <= imc < 40:
    print('Obesidade! com imc de {:.1f}'.format(imc))
else:
    print('Obesidade MÓRBIDA! com imc de {:.1f}'.format(imc))