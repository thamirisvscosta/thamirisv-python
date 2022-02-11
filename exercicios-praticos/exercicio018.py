from math import sin
from math import cos
from math import tan

a = float(input('\033[33m Digite o angulo desejado: '))
s = sin(a)
c = cos(a)
t = tan(a)
print(f'\033[35m O ângulo de {a:.2f} tem o seno de {s:.2f}, o cosseno de {c:.2f} e a tangente de {t:.2f}')