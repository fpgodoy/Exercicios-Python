ext = ('zero', 'um', 'dois', 'três', 'quatro',
'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
'onze', 'doze', 'treze', 'quatorze', 'quinze',
'dezesseis', 'dezessete', 'dezoito', 'dezenove',
'vinte')
rep = 's'
while rep == 's':
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break
        print('Tente novamente.')
    print(f'Você digitou o número {ext[n]}.')
    rep = str(input('Quer continuar? [S/N] '))
print('Programa finalizado.')
