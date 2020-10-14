repeat = 'S'
c = 0
s = 0
maior = 0
menor = 0
print('=-'*20, 'CALCULADORA', '-='*20)
print('Com esta ferramenta, você pode calcular a média de quantos valores quiser.')
print('-'*94)
while repeat != 'N':
    a = s
    c += 1
    n = int(input('Digite o {}º número inteiro:'.format(c)))
    s = a + n
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    repeat = str(input('Deseja informar mais valores? [S/N] ')).upper()
print('='*94)
print('Média dos valores digitados: {}\nMaior valor digitado: {}\nMenor valor digitado: {}'.format(s / c, maior, menor))
print('='*94)
