k = int(input('Quantos quilômetros é sua viagem? '))
if k <= 200:
    k1 = k * 0.50
    print(f'O preço da passagem ficou em R$ {k1:.2f}')
elif k >= 200:
    k2 = k * 0.45
    print(f'Que viagem loonga! Sua passagem ficou em R$ {k2:.2f} ')