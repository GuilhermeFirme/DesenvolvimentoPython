print('Gerador de PA')
print('-==' * 10)
pt = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
pa = pt
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{}'.format(pa), end=' -> ')
        pa = pt + (c * razao)
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))


