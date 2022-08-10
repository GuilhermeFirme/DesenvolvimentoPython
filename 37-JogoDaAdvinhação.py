from random import randint
print('Olá sou seu Computador.\n'
      'Bem-Vindo ao jogo da adivinhação!')
computador = randint(0, 10)
print('Pensei em um número de 0 a 10 tente acertar.')
num = int(input('Qual é sua tentativa? '))
tentativa = 1
if num != computador:
    while num != computador:
        if num < computador:
            print('Mais... Tente mais uma vez.')
        else:
            print('Menos... Tente mais uma vez.')
        num = int(input('Qual é sua tentativa? '))
        tentativa += 1
print('Acertou com {} tentativas. Parabéns!'.format(tentativa))
print('Computador pensou {}!'.format(computador))

