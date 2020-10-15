s = str(input('Digite o sexo da pessoa [F/M] ')).strip().upper()[0]
while s != 'F' and s != 'M':
    s = str(input('Digite F para feminino ou M para masculino: ')).upper()
if s == 'F':
    dado = 'feminino'
elif s == 'M':
    dado = 'masculino'
print('Informação registrada. Você escolheu o sexo {}.'.format(dado))