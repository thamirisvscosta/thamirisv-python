# num = int(input('digite um numero: '))
# u = dez[0]
# d = dez[1]
# c = dez[2]
# m = dez[3]
# print(u)
# print(d)
# print(c)
# print(m)
# esse é um método calculado por strings, porém não funciona se não tiver preenchido todos os valores.

num = int(input('digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
