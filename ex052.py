v = 0
n = int(input('Digite um número inteiro: '))
"""for c in range(2, 10):
    if n % c == 0 and n!=c or n==0:
        v += 1
if v == 0:
    print('O número que você digitou é primo.')
else:
    print('O número que você digitou não é primo.')"""
for c in range (1, n + 1):
    if n % c == 0:
        print('\33[33m', end=' ')
        v += 1
    else:
        print('\33[31m', end=' ')
    print('{}'.format(c), end=' ')
if v != 2:
    print('\n\033[mO número que você digitou não é primo.')
else:
    print('\n\033[mO número que você digitou é primo.')
