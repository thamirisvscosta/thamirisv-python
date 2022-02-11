v = float(input('Qual é o valor da casa? '))
s = float(input('Quanto é o seu salário? '))
a = int(input('Quantos anos pretende pagar a casa? '))
p = v / (a * 12)
s1 = s * 30//100
if s1 > p:
    print(f'O valor da prestação mensal, pagos em {a} anos, '
          f'é de R$ {p:.2f} devido seu salário ser de R${s:.2f} e o valor da casa ser de R$ {v:.2f}')
elif s1 < p:
    print('Infelizmente seu empréstimo foi negado!')
