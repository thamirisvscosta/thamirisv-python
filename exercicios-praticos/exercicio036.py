n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
m = (n1 + n2 + n3) / 3
if m < 4.0:
    print(f'Sua nota é {m:.2f}. Infelizmente você está reprovado! ')
elif 4.0 < m < 6.9:
    print(f'Sua nota é {m:.2f}. Você está de recuperação / prova final. ')
elif m >= 7.0:
    print(f'Sua nota é {m:.2f}.Parabénnss!!! Você está aprovado!!! ')
