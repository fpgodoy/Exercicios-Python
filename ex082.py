valores = list()
pares = list()
impares = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    repeat = input('Deseja informar mais valores? [S/N] ')
    if repeat in 'Nn':
        break
for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 == 1:
        impares.append(valor)
print('-='*10)
print(f'Os valores digitados foram {valores}.')
print(f'Os valores pares são {pares}.')
print(f'Os valores ímpares são {impares}.')
