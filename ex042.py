r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Suas retas podem formar um triângulo.')
    if r1 == r2 == r3:
        print('Seu triângulo é um triângulo equilátero.')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print('Seu triângulo é um triângulo isósceles.')
    else:
        print('Seu triângulo é um triângulo escaleno.')
else:
    print('Suas retas não podem formar um triângulo.')
