from random import randint
num = randint(0,10)
q = 1
chute = int(input ('O computador escolheu um número entre 0 e 10. Tente adivinhar qual foi: '))
while chute != num:
    if chute > num:
        comparado = 'menor'
    elif chute < num:
        comparado = 'maior'
    chute = int(input ('Você errou, o número é {} que esse. Escolha outro número: '.format(comparado)))
    q += 1
print('Parabéns, você acertou, o número era {}. Você precisou de {} tentativas para acertar.'.format(num, q))
