from datetime import date
ano = int(input('Digite o ano de nascimento do atleta:'))
idade = date.today().year - ano
if idade <= 9:
    print('O atleta tem {} anos.'
          '\nEle pertence à categoria MIRIM.'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos.'
          '\nEle pertence à categoria INFANTIL.'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos.'
          '\nEle pertence à categoria JUNIOR.'.format(idade))
elif idade <= 20:
    print('O atleta tem {} anos.'
          '\nEle pertence à categoria SENIOR.'.format(idade))
else:
    print('O atleta tem {} anos.'
          '\nEle pertence à categoria MASTER.'.format(idade))
