from math import sqrt
n = int(input('\033[32m Digite um número: '))
d = n * 2
t = n * 3
r = sqrt(n)
print(f'\033[35m O número digitado foi {n}. Seu dobro é {d}, seu triplo {t} e sua raiz quadrada {r}')
print('\033[34m O valor digitado foi {}. Seu dobro é {},seu triplo é {} e sua raiz quadrada é {}'.format(n, d, t, r))
