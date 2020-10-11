from datetime import date
nasc = int(input('Digite o ano de nascimento:'))
today = date.today()
if int(today.year) - nasc == 18:
    print('É hora de se alistar.'
          '\nProcure uma junta militar.')
elif int(today.year) - nasc > 18:
    print('Já passou a época de se alistar'
          '\nJá se passaram {} anos desde a época correta.'.format((int(today.year) - nasc) - 18))
elif int(today.year) - nasc < 18:
    print('Você ainda precisará se alistar.'
          '\nFaltam {} anos.'.format(18 - (int(today.year) - nasc)))
