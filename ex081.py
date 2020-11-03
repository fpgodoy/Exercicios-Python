valores = list()
while True:
    valores.append(input('Digite um valor: '))
    repeat = input('Deseja informar mais valores? [S/N] ')
    if repeat in 'Nn':
        break
print('-='*10)
print(f'Foram digitados {len(valores)} números.')
valores.sort(reverse=True)
print(f'Os número digitados foram {valores}')
if '5' in valores:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')
