print('=======GERADOR DE SEQUÊNCIA DE FIBONACCI=======')
n = int(input('Quantos elementos você quer? '))
c = n
ultimo = 1
penultimo = 0
print(penultimo, end="")
if c == 1:
    print('.')
else:
    s = 0
    while c != 1:
        c -= 1
        penultimo = ultimo
        ultimo = s
        s = ultimo + penultimo
        print(', {}'.format(s), end="")
    print('.')
