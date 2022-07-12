print('{:-^40}'.format(' LOJAS SOUZA '))
v = float(input('Qual valor das compra: R$ '))
print('Qual forma de pagamento: \n'
      '[1] À vista dinheiro/pix: 10% Desconto\n'
      '[2] À vista no cartão: 5% Desconto \n'
      '[3] Em até 2x no cartão: preço normal\n'
      '[4] 3x ou mais no cartão: 20% Desconto')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    p = v - (v * 0.1)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(v, p))
elif opcao == 2:
    p = v - (v * 0.05)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(v, p))
elif opcao == 3:
    p = v
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(v, p))
elif opcao == 4:
    p = v + v * 0.2
    qtdeParcela = int(input('Quantas parcelas? '))
    valorParcela = p / qtdeParcela
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(qtdeParcela, valorParcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(v, p))
else:
    print('\033[30;41mOpção INVALIDA!\033[m\n'
          'Digite uma das 4 opções')