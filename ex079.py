valores = list()
while True:
    novo = int(input('Digite um valor: '))
    if novo in valores:
        print('Este valor já está na lista.')
    else:
        valores.append(novo)
    repeat = input('Deseja digitar outro valor? [S/N] ')
    if repeat in 'Nn':
        break
valores.sort()
print(f'Os valores digitados foram {valores}.')
