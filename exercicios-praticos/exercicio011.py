l = float(input('\033[36m Digite o valor da largura da área: '))
h = float(input('\033[31m Digite o valor da altura da área: '))
a = l * h
t = a // 2
print(f' A área é {a:.2f} m^2 com {h:.2f}m de altura e {l:.2f}m de largura.\ '
      f'A quantidade de tinta necessária para pintar, em litros, é {t:.2f} L.')