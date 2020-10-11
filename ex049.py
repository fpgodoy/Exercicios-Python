n = int(input('Digite um número para ver a tabuada >>>> '))
for c in range(1, 11):
    print('{:2} X {:2} = {:2}'.format(n, c, n * c))
