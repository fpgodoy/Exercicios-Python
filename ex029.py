vel = int(input('Qual a velocidade do carro? '))
if vel > 80:
    print('Seu carro estava andando a {} km/h e você foi multado.'.format(vel))
    print('Sua multa é de R${:.2f}.'.format((vel - 80) * 7))
else:
    print('Pode passar.')
