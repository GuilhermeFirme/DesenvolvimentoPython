pt = int(input('Qual primeiro termo: '))
razao = int(input('Qual a razão: '))
pa = pt
c = 1
while c <= 10:
    print('{}'.format(pa), end=' -> ')
    pa = pt + (c * razao)
    c += 1

print('ACABOU!!')




