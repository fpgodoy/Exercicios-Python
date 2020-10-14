print('Calculadora de prograssão aritimética.\nImportante: este programam mostra os primeiros 10 termos da progressão.')
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
print('Os primeiros 10 termos da PA apresentada são', end=" ")
while c < 10:
    c += 1
    p = p + r
    print(p, end=", ")
print('{}.'.format(p + r))
