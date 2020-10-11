print('Calculadora de prograssão aritimética.\nImportante: este programam mostra os primeiros 10 termos da progressão.')
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
d = p + (10-1) * r
for c in range(p, d + r, r):
    print(p + c)
