print('Calculadora de progressão aritmética.\nImportante: este programa mostra os 10 primeiros termos da progressão.')
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
print('Os 10 primeiros termos da PA apresentada são ', end="")
while c <= 10:
    print(p,', ' if c < 10 else '.', end = "")
    c += 1
    p += r
print('\n')
