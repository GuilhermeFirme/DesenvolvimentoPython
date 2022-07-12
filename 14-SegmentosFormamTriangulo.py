segmento1 = float(input('Digite o comprimento do primeiro segmento: '))
segmento2 = float(input('Digite o comprimento do segundo segmento: '))
segmento3 = float(input('Digite o comprimento do terceiro segmento: '))
if segmento1 + segmento2 > segmento3 and segmento2 + segmento3 > segmento1 and segmento3 + segmento1 > segmento2:
    print('Os segmentos PODE formam um triângulo!')
else:
    print('\033[4;34;41mSegmentos passados NÃO PODE FORMAR um triângulo!\033[4;34;40m')