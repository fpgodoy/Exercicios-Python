print('{:=^40}'.format('LOJA FICTÍCIA'))
preco = float(input('Digite o preço normal do produto: R$'))
douc = str(input('Selecione a forma de pagamento:'
                 '\n[1] para dinheiro ou cheque'
                 '\n[2] para cartão\n'))
if douc == '1':
    print('O valor à vista, com pagamento em dinheiro ou cheque, terá desconto de 10%, totalizando R${:.2f}.'.format(preco * 90 / 100))
elif douc == '2':
    parc = int(input('Em quantas parcelas no cartão?'))
    if parc == 1:
        print('Com o pagamento à vista no cartão, há desconto de 5%. O preço final será de R${:.2f}.'.format(preco * 95 / 100))
    elif parc == 2:
        print('Parcelado em duas vezes, não há desconto. Serão duas parcelas de R${:.2f}.'.format(preco / 2))
    else:
        print('Parcelado em {} vezes, há juros de 20%. O valor total será R${:.2f}, dividido em {} parcelas de R${:.2f}.'.format(parc, preco * 120 / 100, parc, preco * 120 / 100 / parc))
else:
    print('Sinto muito. Não aceitamos este tipo de pagamento.')
