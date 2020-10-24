from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os números aleatórios gerados foram', end=" ")
maior = menor = numeros[0]
for c in numeros:
    if c > maior:
        maior = c
    if c < menor:
        menor = c
    print(c, end = " ")
print(f'\nO maior número gerado foi {maior} e o menor foi {menor}.')