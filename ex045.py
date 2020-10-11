import random
from time import sleep
seu = str(input('Escolha pedra, papel ou tesoura:'))
opcoes = ['pedra', 'papel', 'tesoura']
sorteio = str(random.choice(opcoes))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
if seu == sorteio:
    print('O computador também escolheu {}. Tivemos um empate.'.format(sorteio))
else:
    print('O computador escolheu {}.'.format(sorteio))
    if (seu == 'papel' and sorteio == 'pedra') or (seu == 'tesoura' and sorteio == 'papel') or (seu == 'pedra' and sorteio == 'tesoura'):
        print('{} ganha de {}. Você ganhou.'.format(seu.capitalize(), sorteio))
    else:
        print('{} ganha de {}. Você perdeu.'.format(sorteio.capitalize(), seu))
