l1 = float(input('Digite a primeira reta:'))
l2 = float(input('Digite a segunda reta: '))
l3 = float(input('Digite a terceira reta: '))
if l1 < l2 + l3 and l2 < l1 +l3 and l3 < l1 + l2:
# lados: a soma dos lados não podem ser maiores entre si (a < b + c)
    print('Pode formar um triângulo!')
else:
    print('\033[31m Desculpe, mas esses valores não podem formar um triângulo')
