from math import cos, sin, tan, radians
a = float(input('Digite um ângulo: '))
print('O seno de um ângulo de {}º é {}.' .format(a, sin(radians(a))))
print('O cosseno de um ângulo de {}º é {}.' .format(a, cos(radians(a))))
print('A tangente de um ângulo de {}º é {}.' .format(a, tan(radians(a))))
