compras = ('Lápis', 100.00, 'Caderno', 5.25, 'Tomate', 8.72, 'Cebola', 1)
print('-' * 59)
print(f'\33[7m{"LISTAGEM DE PREÇOS":^59}\33[m')
print('-' * 59)
for produto in range(0, len(compras), 2):
    print(f'{compras[produto]:.<50}', end = "")
    print(f'\33[31mR${compras[produto + 1]:>7.2f}\33[m')
print('-' * 59)
