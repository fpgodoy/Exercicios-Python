s = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        s += c
        print(c, end=' ')
print('\nA soma de todos os números ímpares divisíveis por 3 no intervalo é {}.'.format(s))
