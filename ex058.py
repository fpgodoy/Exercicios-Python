from random import randint
num = randint(0,10)
q = 1
chute = int(input ('O computador escolheu um número entre 0 e 10. Tente adivinhar qual foi: '))
while chute != num:
    chute = int(input ('Vocẽ errou, tente novamente. Escolha outro número: '))
    q += 1
print('Parabéns, você acertou, o número era {}. Você precisou de {} tentativas para acertar.'.format(num, q))
