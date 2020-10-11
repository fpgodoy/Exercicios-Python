sal = float(input('Qual o salário atual do funcionário? R$'))
if sal > 1250:
    aum = sal * 10 / 100
else:
    aum = sal * 15 / 100
print('O aumento deste funcionário será de R${:.2f}, totalizando o novo salário R${:.2f}.'.format(aum, aum + sal))
