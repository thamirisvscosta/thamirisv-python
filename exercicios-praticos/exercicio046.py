s = 0
for c in range(1,7):
    n = int(input('digite um valor:'))
    if n % 2 == 0:
        s += n
print(f'A soma dos 6 números pares é {s}')