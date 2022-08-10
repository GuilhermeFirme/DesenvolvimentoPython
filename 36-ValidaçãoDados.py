sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
if sexo != 'M' and sexo != 'F':
    while sexo != 'M' and sexo != 'F':  # while sexo not in 'MmFf'
        sexo = str(input('Dados inVálidos. Por favor, informe seu sexo [M/F]: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))



