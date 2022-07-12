n = int(input("Digite um número inteiro: "))
print("Digite [ 1 ] para Binário. \n"
                "Digite [ 2 ] para Octal. \n"
                "Digite [ 3 ] para Hexadecimal. ")
op = int(input("Base escolhida: "))

if op == 1:
    print("A base de conversão Binária para esse número é {}".format(bin(n)[2:]))
elif op == 2:
    print("A base de conversão Octal para esse número é {}".format(oct(n)[2:]))
elif op == 3:
    print("A base de conversão Hexadecimal para esse número é {}".format(hex(n).upper()[2:]))
else:
    print("Digite novamente!")
