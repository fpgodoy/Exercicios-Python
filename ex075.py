valores = (int(input('Digite um número: ')), int(input('Digite um número: ')),
int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'Você digitou os valores {valores}.')
print(f'O número 9 apareceu {valores.count("9")} vezes.')
if 3 not in valores: 
    print('Não foi digitado o número 3.')
else:
    print(f'O número 3 foi digitado na {valores.index(3) + 1}ª posição.')
print('Os números pares foram: ', end = ' ')
for c in valores:
    if c % 2 == 0:
        print(c, end = " ")
