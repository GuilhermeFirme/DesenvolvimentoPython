print('Até 200km cobramos R$0.50 \nAcima de 200km é cobrado R$0.45/km')
km = float(input('Qual a distância  da viagem em KM: '))
print('Você está prestes a fazer uma viagem de {:.2f}KM.'.format(km))
'''if km <= 200:
    v = km * 0.50
    print('Valor da passagem é R${:.2f}'.format(v))
elif km > 200:
    v = km * 0.45'''
v = km * 0.50 if km <= 200 else km * 0.45
print('Valor da passagem é R${:.2f}'.format(v))
