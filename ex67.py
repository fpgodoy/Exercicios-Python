while True:
    n = int(input('Digite um número para ver a tabuada (um número negativo encerra o programa): '))
    print('-'*78)
    if n < 0:
        break
    for t in range(1, 11):
        print(f'{n} x {t:2} = {n * t:2}')
    print('-'*78)
print('Programa finalizado.')
