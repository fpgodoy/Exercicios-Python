frase = input('Digite uma frase: ').strip().upper()
print('Na sua frase a letra A aparece {} vezes.'.format(frase.count('A')))
print('A letra A aparece pela primeira vez na sua frase na posição {}.'.format(frase.find('A')))
print('A letra A aparece pela última vez na sua frase na posiçao {}.'.format(frase.rfind('A')))
