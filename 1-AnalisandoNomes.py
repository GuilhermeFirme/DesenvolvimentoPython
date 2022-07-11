nome = str(input('Digite Seu Nome:')).strip()
print('Analisando seu nome...')
print('com letras maiscula: {0},'
      '\n'
      'com letras minuscula: {1}, \n'
      'Seu nome tem ao todo {2} letras, \n'
      'Seu primeiro nome tem {3} letras'.format(nome.upper(), nome.lower(), len(nome) - nome.count(' '), nome.find(' ')))
