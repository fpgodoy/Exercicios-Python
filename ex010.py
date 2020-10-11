rs = float(input('Quantos reais você tem na carteira? >>> '))
us = float(3.27)
print('Com o dinheiro que você tem na carteira, considerando uma taxa de câmbio de R${}, você pode comprar U${:.2f}'.format(us, rs/us))
