from math import sqrt, hypot
c1 = float(input('Digite a medida do cateto oposto:  '))
c2 = float(input('Digite a medida do cateto adjacente:  '))
h = sqrt(c1**2 + c2**2)
print('A hipotenusa deste triângulo mede {}.'.format(h))
print('A hipotenusa deste triângulo mede {}.'.format(hypot(c1, c2)))
