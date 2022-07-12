''''segmento1 = float(input('Digite o comprimento do primeiro segmento: '))
segmento2 = float(input('Digite o comprimento do segundo segmento: '))
segmento3 = float(input('Digite o comprimento do terceiro segmento: '))
equi = segmento1 == segmento2 and segmento2 == segmento3
iso = segmento1 == segmento2 or segmento1 == segmento3 or segmento2 == segmento3
escaleno = segmento1 != segmento2 != segmento3

if segmento1 + segmento2 > segmento3 \
        and segmento2 + segmento3 > segmento1 \
        and segmento3 + segmento1 > segmento2 \
    and equi:
    print('Os segmentos PODE formam um triângulo \033[;31;40mEQUILÁTERO!\033[m')

elif segmento1 + segmento2 > segmento3 \
        and segmento2 + segmento3 > segmento1 \
        and segmento3 + segmento1 > segmento2 \
    and iso:
    print('Os segmentos PODE formam um triângulo \033[;31;40mISÓCELES!\033[m')


elif segmento1 + segmento2 > segmento3 \
        and segmento2 + segmento3 > segmento1 \
        and segmento3 + segmento1 > segmento2 \
    and escaleno:
    print('Os segmentos  PODE FORMAR um triângulo \033[;31;40mESCALENO!\033[m')

else:
    print('\033[;37;40mOs segmentos fornecidos não formam um triângulo\033[m')'''''

segmento1 = float(input('Digite o comprimento do primeiro segmento: '))
segmento2 = float(input('Digite o comprimento do segundo segmento: '))
segmento3 = float(input('Digite o comprimento do terceiro segmento: '))

if segmento1 + segmento2 > segmento3 \
        and segmento2 + segmento3 > segmento1 \
        and segmento3 + segmento1 > segmento2:
    print('Os segmentos PODEM formar um triângulo ', end = '')

    if segmento1 == segmento2 == segmento3:
        print('\033[;31;40mEQUILÁTERO!\033[m')

    elif segmento1 == segmento2 or segmento1 == segmento3 or segmento2 == segmento3:
        print('\033[;31;40mISÓCELES!\033[m')

    else:
        print('\033[;31;40mESCALENO!\033[m')

else:
    print('\033[;37;40mOs segmentos fornecidos não formam um triângulo\033[m')