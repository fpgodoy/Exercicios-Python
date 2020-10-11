s = 0
print('Digite o ano de nascimento de 7 pessoas.')
for c in range(0, 7):
    p = int(input('Ano de nascimento: '))
    if 2020 - p >= 18:
        s += 1
print('Das pessoas digitadas, {} ainda não alcançaram a maioridade e {} já são maiores de idade.'.format(7-s, s))
