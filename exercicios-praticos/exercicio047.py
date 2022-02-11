from time import sleep
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite o valor da razão:  '))
d = a1 + (10 - 1) * r
for c in range(a1,d + r, r):
    print(c)
    sleep(0.25)
print('Acabou!')