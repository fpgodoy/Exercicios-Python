casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valor do salário: R$'))
prazo = int(input('Qual o prazo de pagamento em anos?'))
mensal = casa / (prazo * 12)
if mensal < salario * 30 / 100:
    print('Seu financiamento será aprovado.\nO valor da parcela mensal será de R${:.2f}.'.format(mensal))
else:
    print('Infelizmente não poderemos financiar sua casa.')
