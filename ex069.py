mais18 = men = w20 = 0
while True:
    print('-' * 19)
    print('CADASTRE UMA PESSOA')
    print('-' * 19)
    idade = int(input('Idade: '))
    sexo = cont = 'a'
    while sexo not in 'MF':
        sexo = str(input ('Sexo: [M/F] ')).upper().strip()[0]
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        men += 1
    if sexo == 'F' and idade < 20:
        w20 += 1
    print('-' * 19)
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    print('-' * 19)
    if cont == 'N':
        break
print('=' * 6, 'FIM DO PROGRAMA', '=' * 6)
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Total de homens: {men}')
print(f'Total de mulheres com menos de 20 anos: {w20}')
