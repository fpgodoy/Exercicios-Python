n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1 + n2) / 2
if media < 5:
    print('Sua média foi {}. Você foi reprovado.'.format(media))
elif media >= 7:
    print('Sua média foi {}. Voce foi aprovado.'.format(media))
else:
    print('Sua média foi {}. Você ficou de recuperação.'.format(media))
