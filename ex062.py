print('Calculadora de prograssão aritimética.\nImportante: este programam mostra os primeiros 10 termos da progressão.')
repeat = ''
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
while repeat != 0:
    c = 1
    if repeat == '':
        repeat = 10
        print('Os 10 primeiros termos da PA apresentada são', end=" ")
    else:
        print('Segue abaixo os termos adicionais solicitados:')
    if repeat != 1:
        while c < repeat:
            c += 1
            p = p + r
            print(p, end=", ")
    p = p + r
    print('{}.'.format(p))
    print('==='* 30)
    repeat = int(input('Deseja mostrar mais quantos termos? Digite 0 para encerrar.'))
print('....'*30)
print('Programa encerrado.')
