frase = str(input('Digite uma frase: ')).strip().upper()
frase.upper()
print('Quantas vezes aparece a letra A: {0} \n'
    'Em qual posição aparece primeira vez: {1}\n'
    'A última vez que aparece: {2}'.format(frase.count('A'), frase.find('A'), frase.rfind('A')))
