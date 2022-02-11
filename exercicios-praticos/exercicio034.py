n1 = int(input('Digite um número: '))
n2 = int(input('Digite um outro número: '))
if n1 > n2:
    print(f'O primeiro valor ({n1}) é maior!')
elif n2 > n1:
    print(f'O segundo valor ({n2}) é maior!')
elif n2 == n1:
    print(f' Não existe valores maiores! Os dois são iguais. ')