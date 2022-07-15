num = int(input('Digite a tabuada desejada: '))
resultado = int
for n in range(1, 11):
    resultado = num * n
    print('{} X {} = {}'.format(n, num, resultado))#outra forma de fazer: num*n
