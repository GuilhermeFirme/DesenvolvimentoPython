continuar = ''
media = soma = 0.0
cont = 0
menor = maior = n = 0
while continuar in 'Ss':
    n = int(input('Digite um número: '))
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    soma += n
    cont += 1
    continuar = str(input('Quer continuar? [S/N]'))
media = soma / cont
print('Você digitou {} números e a média foi {:.2f}'.format(cont, media))
print('O maior valor digitado foi {} e o menor {}'.format(maior, menor))