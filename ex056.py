somaidade = 0
q = int(input('Quantas pessoas você quer cadastrar?'))
velho = 0
idadevelho = 0
mulhernova = 0
for c in range(1, q + 1):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(c)))
    idade = int(input('Digite a idade da {}ª pessoa: '.format(c)))
    sexo = str(input('Informe o Sexo da {}ª [M/F]: '.format(c)))
    somaidade += idade
    if sexo == 'M' and c == 1:
        idade = idadevelho
        velho = nome
    elif sexo == 'M' and c != 1 and idade > idadevelho:
        velho = nome
        idadevelho = idade
    if sexo == 'F' and idade < 20:
        mulhernova += 1
print('A médidas idades informadas é {}.'.format(somaidade / q))
print('O homem mais velho se chamada {} e tem {} anos.'.format(velho, idadevelho))
print('Dentre as pessoas informadas, {} são mulheres com menos de 20 anos.'.format(mulhernova))
