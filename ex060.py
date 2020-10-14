from time import sleep
print('===' * 30)
repeat = 'S'
while repeat == 'S': 
    n = int(input('Digite um número para calcular seu fatorial: !'))
    modo = str(input('Escolha como quer que seja calculado (F para usar a função for e W para usar a função While): ')).upper()
    print('processando...')
    sleep(2)
    print('---' * 30)
    if modo == 'F':
        res = n
        modo = 'FOR'
        for f in range(res - 1, 1, -1):
            res = res * f
    elif modo == 'W':
        res = n
        cont = res
        modo = 'WHILE'
        while cont > 1:
            cont = cont-1
            res = res * cont
    print('O fatorial de {} calculado com a função {} é {}.'.format(n, modo, res))
    repeat = str(input(('Deseja fazer um novo cálculo? [S/N] '))).upper()
    print('---' * 30)
print('FIM')
