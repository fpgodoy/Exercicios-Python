from time import sleep
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
print('Qual operação vocẽ quer realizar com os números digitados?')
print('[1] somar\n[2] multiplicar\n[3] maior\n[4] informar novos números\n[5] sair do programa')
op = int(input('Digite uma das opções do menu: '))
while op != 5:
    print('Processando operação...')
    sleep(1)
    if op == 1:
        print('***'*10)
        print('A soma dos valores é {}.'.format(v1 + v2))
    if op == 2:
        print('***'*10)
        print('A multiplicação dos valores digitados totaliza {}.'.format(v1 * v2))
    if op == 3:
        print('***'*10)
        if v1 > v2:
            print('O maior número digitado foi {}.'.format(v1))
        elif v1 == v2:
            print('Os dois números digitados são iguais.')
        else:
            print('O maior número digitado foi {}.'.format(v2))
    if op == 4:
        v1 = int(input('Digite o primeiro valor: '))
        v2 = int(input('Digite o segundo valor: '))
    print('==='*10)
    sleep(1)
    print('Quer realizar outra operação com os números digitados?')
    print('[1] somar\n[2] multiplicar\n[3] maior\n[4] informar novos números\n[5] sair do programa')
    op = int(input('Digite uma das opções do menu: '))
print('Obrigado por usar nossa calculadora. Este programa está sendo encerrado.')
sleep(2)
print('Programa encerrado. FIM')