valores = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'Você digitou os valores {valores}.')
print('O número 9 apareceu {} vezes.'.format(valores.count(9)))
if 3 not in valores: 
    print('Não foi digitado o número 3.')
else:
    print('O número 3 foi digitado na {}ª posição.'.format(valores.index(3) + 1))
print('Os números pares foram: ')
for c in valores:
    if c % 2 == 0:
        print(c, end = " ")
