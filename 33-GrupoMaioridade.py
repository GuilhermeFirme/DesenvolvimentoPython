from datetime import date
atual = date.today().year
maiores = 0
menores = 0
for c in range(1, 8):
    nasc = int(input('Em que ano a {} pessoa nasceu? '.format(c)))
    idade = atual - nasc
    if idade > 18:
        maiores += 1
    else:
        menores += 1
print('Ao todo tivemos {} pessoa maiores de idade.\n'
      'E também tivemos {} pessoas menores de idade.'.format(maiores, menores))




