s1 = float(input('\033[36m Digite o seu salário aqui: '))
s2 = (s1 * 15)/100
s3 = s1 + s2
print('\033[34m O seu novo salário é {:.2f} reais com 15% de aumento.'
      'Anteriormente, seu salário era de {:.2f} reais.'.format(s3, s1))
print(f'\033[35m O seu novo salário é {s3:.2f} reais com 15% de aumento.' 
      'Anteriormente, seu salário era de {s1:.2f} reais')
