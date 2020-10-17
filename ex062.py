print('Calculadora de progressão aritmética.')
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
    while c <= repeat:
        print('{}{}'.format(p, ', ' if c < repeat else '.'), end = "")
        c += 1
        p += r
    print('\n', '==='* 30)
    repeat = int(input('Deseja mostrar mais quantos termos? Digite 0 para encerrar. >>>> '))
print('...'*30)
print('Programa encerrado.')
