from time import sleep
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
op = int
while op != 5:
    print('[1] Somar\n'
          '[2] Multiplicar\n'
          '[3] Maior\n'
          '[4] Novos números\n'
          '[5] Sair do programa')
    op = int(input('>>>>>> Qual é sua opção? '))
    if op == 1:
        resultado = num1 + num2
        print('A soma entre de {} + {} é {}'.format(num1, num2, resultado))
        print('=-=' * 10)
    elif op == 2:
        resultado = num1 * num2
        print('A multiplicação de {} x {} é {}'.format(num1, num2, resultado))
        print('=-==' * 10)
    elif op == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('Entre os números {} e {} o maior valor é {}'.format(num1, num2, maior))
        print('=-==' * 10)
    elif op == 4:
        print('Informe os Números Novamente:')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif op == 5:
        exit(print('Fim do programa. Volte sempre!'))

    else:
        print('Opção invalida! Tente novamente.')
    sleep(2)

print('Fim do programa. Volte sempre!')
