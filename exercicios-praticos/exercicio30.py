e = int(input('digite o primeiro valor: '))
f = int(input('digite o segundo valor: '))
g = int(input('digite o terceiro valor: '))
if e > f and e > g:
    if f > g:
        print(f'O maior número é {e} e o menor número é {g}')
    elif f < g:
        print(f'O maior número é {e} e o menor número é {f}')
elif f > e and f > g:
    if e > g:
        print(f'O maior número é {f} e o menor número é {g}')
    elif g > e:
        print(f'O maior número é {f} e o menor número é {e}')
elif g > e and g > f:
    if e > f:
        print(f'O maior número é {g} e o menor número é {f}')
    elif e < f:
        print(f'O maior número é {g} e o menor número é {e}')
