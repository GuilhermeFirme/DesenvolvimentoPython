print('\033[;31;42m=========================SISTEMA DE NOTAS=========================\033[m')
nome = str(input('Qual o nome do aluno: '))
n1 = float(input('Digite a nota 1 do aluno: '))
n2 = float(input('Digite a nota 2 do aluno:'))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))
if media < 5:
    print('{}, Você Não alcançou a nota media de 5 REPROVADO!. com nota {}'.format(nome, media))

elif 7 > media >= 5:
    print('{}, você ficou de RECUPERAÇÃO!'.format(nome))

elif media >= 7:
    print('Parabéns {}, você foi APROVADO! NOIA...'.format(nome))
