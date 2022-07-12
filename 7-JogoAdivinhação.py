from random import randint
computador = randint(0, 5)
print('-**-' * 20)
print('Vou pensar em um número entre 0 e 5 Tente adivinhar...')
print('-**-' * 20)
n = int(input('Em qual número eu pensei: ')) #Numero que o jogador tentou adivinhar
if n != computador:
    print('Eu Venci você: {0}'.format(computador))
else:
    print('Parábens você venceu: {0}'.format(n))