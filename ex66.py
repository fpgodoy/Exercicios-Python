c = s = 0
while True:
    n = int(input('Digite um número (999 faz parar): '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Você digitou {c} números, cuja soma é {s}.')
