n = 0
c = -1
s = n
print('=-'*21, 'SOMADORA', '-='*21)
print('Você pode somar quantos números quiser. Quando quiser encerrar e saber o resultado, digite 999.')
print('-'*94)
while n != 999:
    a = s
    c +=1
    n = int(input('Digite um número inteiro:'))
    s = a + n
print('='*94)
print('Quantidade de números digitados: {}\nSoma dos números digitados: {}'.format(c, s - 999))
print('='*94)
