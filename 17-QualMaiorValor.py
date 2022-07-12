n1 = int(input("Digite primeiro número: "))
n2 = int(input("Digite segundo numero: "))
if n1 > n2:
    print('Primeiro valor {} é maior!'.format(n1))
elif n2 > n1:
    print('Segundo valor {} é maior!'.format(n2))
else:
    print("não existe valor maior, os dois são iguais.")