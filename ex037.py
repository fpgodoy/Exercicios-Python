numero = int(input('Digite um número inteiro: '))
base = int(input('Qual a base de conversão desejada?'
                 '\n[1] converter para binário'
                 '\n[2] converter para octal'
                 '\n[3] converter para hexadecimal.\n'))
if base == 1:
    tipo = 'binária'
    print('O número digitado, convertido para base {} é {}.'.format(tipo, bin(numero)[2:]))
elif base == 2:
    tipo = 'octal'
    print('O número digitado, convertido para base {} é {}.'.format(tipo, oct(numero)[2:]))
elif base == 3:
    tipo = 'hexadecimal'
    print('O número digitado, convertido para base {} é {}.'.format(tipo, hex(numero)[2:]))
else:
    print('Opção inexistente.')
