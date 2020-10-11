f = str(input('Digite uma frase:')).upper()
i = f[::-1]
if i.replace(' ', '') == f.replace(' ', ''):
    print('{} ao contrário é {}. A frase é um palíndromo.'.format(i.replace(' ', ""), f.replace(' ', '')))
else:
    print('Sua frase digitada não é um palíndromo.')