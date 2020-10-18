print('=' * 30)
print('CAIXA ELETRÔNICO')
print('=' * 30)
valor = int(input('Qual o valor do saque? R$'))
while True:
    cinq = vinte = dez = um = 0
    cinq = int(valor / 50)
    if cinq > 0:
        print(f'Total de {cinq} cédulas de R$50')
    if valor % 50 == 0:
        break
    valor = valor % 50
    vinte = int(valor / 20)
    if vinte > 0:
        print(f'Total de {vinte} cédulas de R$20')
    if valor % 20 == 0:
        break
    valor = valor % 20
    dez = int(valor / 10)
    if dez > 0:
        print(f'Total de {dez} cédulas de R$10')
    if valor % 10 == 0:
        break
    valor = valor % 10
    um = valor
    print(f'Total de {um} cédulas de R$1')
    break
print('=' * 30)
print('Obrigado e volte sempre.')
