times = ('Internacional', 'Flamengo', 'Atlético-MG', 'São Paulo', 'Santos',
'Fluminense', 'Fortaleza', 'Palmeiras', 'Atlético-GO', 'Corinthians',
'Grêmio', 'Sport Recife', 'Bahia', 'Ceará SC', 'Botafogo', 'Vasco da Gama',
'Athletico-PR', 'Coritiba', 'Bragantino-SP', 'Goiás')
print('-='*15)
print(f'Os 5 primeiros colocados no Campeonato Brasileiro são {times[:5]}.')
print('-='*15)
print(f'Os últimos 4 colocados são {times[-4:]}.')
print('-='*15)
print(f'Os times que estão competindo, em ordem alfabética, são {sorted(times)}.')
print('-='*15)
print(f'O time do Coritiba está em {times.index("Coritiba") + 1}ª posição.')
