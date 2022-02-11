p = str(input('digite uma frase: ')).strip().upper()
t = p.split()
g = ''.join(t)
j = g[::-1]
print(f'O inverso de {g} é {j}. ')
if g == j:
    print(' logo É UM PALÍNDROMO!')
else:
    print('logo NÃO É UM PALÍNDROMO!')