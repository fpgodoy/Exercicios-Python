from random import randint
v = 0
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
while True:
    comp = randint(0, 10)
    jog = str(input('Escolha par ou ímpar [P/I]: ')).upper().strip()[0]
    while jog not in 'PI':
        jog = str(input('Escolha par ou ímpar [P/I]: ')).upper().strip()[0]
    if jog == 'P':
        jog = 'PAR'
    elif jog == 'I':
        jog = 'ÍMPAR'
    n = int(input('Escolha o seu número: '))
    if n > 10:
        n = int(input('O número precisa ser entre 0 e 10: '))
    s = n + comp
    if s % 2 == 0:
        pi = 'PAR'
    else:
        pi = 'ÍMPAR'
    if jog == pi:
        res = 'venceu'
        v += 1
    else:
        res = 'perdeu'
    print('-'*40)
    print(f'Você escolheu {jog}.')
    print(f'O computador jogou {comp} e você jogou {n}. Total de  {s}. DEU {pi}.')
    print(f'Você {res}.')
    print('-' * 40)
    if res == 'perdeu':
        break
    print('Vamos jogar novamente...')
    print('=-' * 20)
print(f'Jogo encerrado. Total de vitórias: {v}')
