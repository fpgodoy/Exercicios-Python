c = input('Digite alguma coisa: ')
t = 'O dado digitado'
print('Você digitou {}.'.format(c))
print('O tipo primitivo do dado digitado é {}.'.format(type(c)))
print(t, 'é alfanumérico?', c.isalnum())
print(t, 'é alfabético?', c.isalpha())
print(t, 'é ascii?', c.isascii())
print(t, 'é decimal?', c.isdecimal())
print(t, 'é digitável?', c.isdigit())
print(t, 'é identificador?', c.isidentifier())
print(t, 'é minúsculo?', c.islower())
print(t, 'é numérico?', c.isnumeric())
print(t, 'é imprimível?', c.isprintable())
print(t, 'só tem espaços?', c.isspace())
print(t, 'está capitalizada?', c.istitle())
print(t, 'é maiúsculo?', c.isupper())
