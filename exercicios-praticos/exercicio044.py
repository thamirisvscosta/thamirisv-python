s = 0
for c in range(0,501,3):
    print(c)
    if c % 2 == 1:
        s += c
print(f'a soma dos números ímpares múltiplos de 3 é {s}')

# soma = 0
# cont = 0
#  for c in range(1, 501, 2):
#       if c % 3 == 0:
#           cont = cont + 1
#           soma = soma + c
# print('A soma dos números impares multiplos de 3 é {}'.format(soma))