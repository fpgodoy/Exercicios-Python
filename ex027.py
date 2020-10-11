nome = str(input('Digite seu nome completo: ')).strip()
sp = nome.split()
#qnt = int(len(sp)) - 1
print('O seu primeiro nome é {}.'.format(sp[0]))
#sp.reverse()
#print('O seu último nome é {}.'.format(sp[0]))
print('O seu último nome é {}.'.format(sp[len(sp) - 1]))
