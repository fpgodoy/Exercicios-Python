valores = list()
for c in range(0,5):
    print(f'Digite um valor para a posição {c}', end = '')
    valores.append(input(': '))
print(f'O maior valor digitado foi {max(valores)}, que aparece nas posições ', end = '')
for chaveMaior, valorMaior in enumerate(valores):
    if valorMaior == max(valores):
        print(f'{chaveMaior} ', end = '')
print(f'\nO menor valor digitado foi {min(valores)}, que aparece nas posições ', end = '')
for chaveMenor, valorMenor in enumerate(valores):
    if valorMenor == min(valores):
        print(f'{chaveMenor} ', end = '')
print('\nPrograma encerrado.')