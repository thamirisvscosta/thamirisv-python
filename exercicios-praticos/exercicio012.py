p1 = float(input('\033[31m Digite o preço do produto: '))
p2 = (p1 * 5) / 100
p3 = p1 - p2
print(f'\033[36m O valor do produto é {p1:.2f} reais e com 5% de desconto sai por {p3:.2f} reais. ')
print('\033[34m O valor do produto é {:.2f} reais e com 5% de desconto sai por {:.2f} reais.'.format(p1, p3))
