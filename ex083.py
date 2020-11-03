expressao = input('Digite uma expressão matemática com parênteses: ')
abertos = expressao.count('(')
fechados = expressao.count(')')
if abertos == fechados:
    print('Expressão válida.')
else:
    print('Expressão inválida.')