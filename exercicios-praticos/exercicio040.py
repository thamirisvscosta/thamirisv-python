d = float(input('digite o valor do produto: '))
t = str(input('digite o tipo de pagamento: [vc = à vista (cartão) ; vd  = à vista (dinheiro/cheque); '
              ' c1 = 2x (cartão); c2 = 3x ou mais (cartão) ] '))
d1 = d * 5//100
d2 = d - d1
d3 = d * 10//100
d4 = d - d3
d5 = d * 20//100
d6 = d + d5
if t == 'vc':
    print(f'Seu pagamento foi à vista no cartão. Você pagará R${d2:.2f} com 5% de desconto. ')
elif t == 'vd':
    print(f'Seu pagamento foi à vista em dinheiro/cheque. Você pagará R${d4:.2f} com 10% de desconto ')
elif t == 'c1':
    print(f'Seu pagamento foi 2x no cartão. Você pagará R${d:.2f}. ')
elif t == 'c2':
    g = int(input('Digite o valor da prestação: '))
    print(f'Seu pagamento foi {g}x no cartão. Você pagará R$ {d6:.2f} com 20% de juros.')