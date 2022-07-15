soma = 0
num = int
cont = 0
for n in range(1, 7):
    num = int(input('Digite {} número: '.format(n)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('A soma dos {} numeros PARES é {}'.format(cont, soma))