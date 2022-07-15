pt = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = pt + (11 - 1) * razao
for c in range(pt, decimo, razao):
    print('{}'.format(c), end='-> ')
print('ACABOU')
