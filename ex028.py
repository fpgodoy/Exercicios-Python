from random import randint
num = randint(0,9)
chute = int(input ('O computador escolheu um número entre 0 e 9. Tente adivinhar qual foi: '))
print('Você escolheu {}.'.format(chute))
if chute == num:
    print('Parabéns, você acertou, o número era {}.'.fomart(num))
else:
    print('Você errou, o número era {}.'.format(num))
