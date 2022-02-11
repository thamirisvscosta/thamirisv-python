v = int(input('\033[34m Escreva um valor em metros: '))
c = v * 100
m = v * 1000
print(f'\033[31m O valor em metros digitado foi {v}. Em centímetros temos {c} e em milímetros temos {m}')
print('\033[36m O valor em metros digitado foi {}. Em centímetros temos {} e em milímetros temos {}'.format(v, c, m))