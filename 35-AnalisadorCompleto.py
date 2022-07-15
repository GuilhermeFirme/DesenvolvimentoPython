media = 0
maisv = 0
n = str
cont = 0
for p in range(1, 5):
    print('----- {}ª Pessoa -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    media += idade / 4
    if p == 1 and sexo in 'Mm':
        maisv = idade
        n = nome
    if idade > maisv and sexo in 'Mm':
        maisv = idade
        n = nome
    if idade < 20 and sexo == 'F':
        cont += 1

print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maisv, n))
print('Ao todo são {} mulheres com menos de 20 anos'.format(cont))
