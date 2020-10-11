peso = float(input('Digite seu peso:'))
altura = float(input('Digite sua altura:'))
imc = peso / altura ** 2
if imc < 18.5:
    print('Seu imc é {:.2f}. Você está abaixo do seu peso ideal.'.format(imc))
elif imc <= 25:
    print('Seu imc é {:.2f}. Você está no peso ideal.'.format(imc))
elif imc <= 30:
    print('Seu imc é {:.2f}. Você está em sobrepeso.'.format(imc))
elif imc <= 40:
    print('Seu imc é {:.2f}. Você está obeso.'.format(imc))
elif imc > 40:
    print('Seu imc é {:.2f}. Você está em obesidade mórbida.'.format(imc))
