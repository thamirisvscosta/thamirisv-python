n = int(input('\033[35m digite um número: '))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        t += 1
    else:
        print('\033[31m', end='')
print(f'\033[36m O número {n} foi divisível {t} vezes')
if t == 2:
    print('e por isso ele É PRIMO!')
else:
    print('e por isso ele NÃO É PRIMO!')
