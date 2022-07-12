from datetime import date
ano = int(input('Qual seu ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print('Você tem {} anos'.format(idade))
if idade <= 9:
    print('Sua categoria é \033[;31;40mMIRIM\033[m')

elif 9 < idade <=14:
    print('Sua categoria é \033[;31;40mINFANTIL\033[m')

elif 14 < idade <= 19:
    print('Sua categoria é \033[;31;40mJÚNIOR\033[m')

elif 19 < idade <= 25:
    print('Sua categoria é \033[;31;40mSÊNIOR\033[m')

else:
    print('Sua categoria é \033[;31;40mMASTER\033[m')