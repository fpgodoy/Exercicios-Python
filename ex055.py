lista = []
for c in range (0, 5):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    lista.append(peso)
print('Das pessoas informadas, o maior peso foi {} e o menor foi {}.'.format(max(lista), min(lista)))
