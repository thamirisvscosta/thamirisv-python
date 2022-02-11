d = int(input('\033[34m Por quantos dias foi alugado o carro? '))
k = int(input('\033[35m Quantos quilômetros foram rodados? '))
d1 = 60 * d
k1 = 0.15 * k

p = d1 + k1
print('\033[36m O valor total a pagar é de R$ {:.2f} por '
      'aluguel de {:.0f} dias e {:.1f} quilômetros gastos.'.format(p, d, k))

