n1 = int(input('digite um valor inteiro: '))
t = str(input('qual base você deseja converter: [bi, oct, hex]  '))
if t == 'bi':
    n2 = bin(n1)
    print(f'\033[36m O número {n1} em base binária é {n2}!')
elif t == 'oct':
    n3 = oct(n1)
    print(f'\033[36m O número {n1} em base octal é {n3}!')
elif t == 'hex':
    n4 = hex(n1)
    print(f'\033[36m O número {n1} em base hexadecimal é {n4}!')