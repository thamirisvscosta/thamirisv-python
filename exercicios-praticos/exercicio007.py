n1 = float(input('\033[31m Digite a primeira nota: '))
n2 = float(input('\033[35m Digite a segunda nota: '))
n = (n1 + n2)/2
print(f'\033[32m Somando sua primeira nota {n1} e sua segunda nota {n2}, sua média na disciplina é {n}')
print('\033[34m Somando sua primeira nota {} e sua segunda nota {}, sua média na disciplina é {}'.format(n1, n2, n))
