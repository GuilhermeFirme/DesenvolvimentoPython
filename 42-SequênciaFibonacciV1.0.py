print('-' * 40)
print('SEQUÊNCIA DE FIBONACCI')
print('-' * 40)
termos = int(input('Quantos termos você quer mostrar? '))
a = 0
b = 1
print('{} -> {}'.format(a, b), end='')
cont = 3
while cont <= termos:
    c = a + b
    print(' -> {}'.format(c), end='')
    a = b
    b = c
    cont += 1
print(' -> FIM!')
print('-' * (termos * 6))





