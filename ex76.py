compras = ('Lápis', 100.00, 'Caderno', 5.25, 'Tomate', 8.72, 'Cebola', 1)
print('-' * 59)
print('\33[7mLISTAGEM DE PREÇOS\33[m'.center(59))
print('-' * 59)
for produto in range(0, len(compras), 2):
    print('{}'.format(compras[produto]).ljust(50, "."), end = "")
    print('\33[31mR${:7.2f}\33[m'.format(compras[produto + 1]))
print('-' * 59)
