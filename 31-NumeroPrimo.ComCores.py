num = int(input('Digite um número: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[35m', end='')
        tot += 1
    else:
        print('\033[m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('O \033[35m{}\033[m é um número primo'.format(num))
else:
    print('O {} NÃO é um número PRIMO'.format(num))


