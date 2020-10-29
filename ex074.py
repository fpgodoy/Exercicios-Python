from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10),
randint(0, 10), randint(0, 10))
print(f'Os números sorteados foram {numeros}.')
print(f'O maior número sorteado foi {max(numeros)} e o menor foi {min(numeros)}.')
