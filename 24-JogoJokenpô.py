from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('Suas opções: \n'
      '[ 0 ] PEDRA.\n'
      '[ 1 ] PAPEL.\n'
      '[ 2 ] TESOURA.')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('=-' * 20)
print('Computador escolheu {}'.format(itens[computador]))
print('Jogador  jogou {}'.format(itens[jogador]))
print('=-' * 20)

if computador == jogador:
      print('Empate!')
elif computador == 0 and jogador != 1: #computador jogou pedra
      print('COMPUTADOR VENCE!')
elif computador == 1 and jogador != 2: #computador jogou papel
      print('COMPUTADOR VENCE!')
elif computador == 2 and jogador != 0: #computador jogou tesoura
      print('COMPUTADOR VENCE')
else:
      print('JOGADOR VENCE')