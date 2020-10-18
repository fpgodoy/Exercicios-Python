print('=' * 30)
print('{:^30}'.format('CAIXA ELETRÔNICO'))
print('=' * 30)
valor = int(input('Qual o valor do saque? R$'))
ced = 50
while True:
    qced = int(valor / ced)
    if qced > 0:
        print(f'Total de {qced} cédulas de R${ced}')
    if valor % ced == 0:
        break
    else:
        valor = valor % ced
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1    
print('=' * 30)
print('Obrigado e volte sempre.')
