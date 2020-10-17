s = c = 0
print('=-'*21, 'SOMADORA', '-='*21)
print('Você pode somar quantos números quiser. Quando quiser encerrar e saber o resultado, digite 999.')
print('-'*94)
n = int(input('Digite um número inteiro:'))
while n != 999:
    c +=1
    s += n
    n = int(input('Digite um número inteiro:'))
print('='*94)
print('Quantidade de números digitados: {}\nSoma dos números digitados: {}'.format(c, s))
print('='*94)
