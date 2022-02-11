from math import sqrt
b = int(input('digite um valor para o cateto oposto: '))
c = int(input('digite outro valor para o cateto adjacente: '))
a = sqrt(((b**2)+(c**2)))
print('o valor da hipotenusa com o cateto oposto sendo {:.2f} e '
      'o cateto adjacente sendo {:.2f} é {:.2f}'.format(b, c, a))
