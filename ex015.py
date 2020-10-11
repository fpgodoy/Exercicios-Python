d = int(input('Quantos diárias de locação? >>> '))
k = float(input('Quantos quilômetros foram rodados? >>> '))
diarias = d * 60
quilo = k * 0.15
print('O valor total devido para {} diárias e {}km rodados é de R${:.2f}.'.format(d, k, diarias + quilo))
