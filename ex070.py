total = mais = pricebarato = 0
barato = ''
print('-' * 40)
print('{:^40}'.format('LOJA SUPER BARATÃO'))
print('-' * 40)
while True:
    nome = str(input('Nome do Produto: '))
    price = float(input('Preço: R$'))
    if total == 0:
        pricebarato = price
    total += price
    if price > 1000:
        mais += 1
    if price <= pricebarato:
        barato = nome
        pricebarato = price
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if cont == 'N':
        break
print('-' * 40)
print('Fechando sua compra...')
print('-' * 40)
print(f'Total gasto na compra: R${total:.2f}')
print(f'Produtos que custaram mais de R$1000.00: {mais}')
print(f'Produto mais barato: {barato}, que custou R${pricebarato:.2f}')
