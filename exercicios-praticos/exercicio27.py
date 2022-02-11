import random
c = random.randint(0, 5)
r = int(input('\033[0m Que número eu pensei? '))
if r == c:
    print('\033[0;36; m Parabéns!!!!! você acertou! ;) ')
elif r != c:
    print('\033[0;31; m Caraca,muito burro! Você errou! :D')