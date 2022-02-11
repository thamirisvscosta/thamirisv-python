n= int(input('\033[31m Digite um número: '))
n1= n-1
n2= n+1
print(f'\033[36m Você digitou o valor {n}. Seu sucessor é {n2} e o antecessor é {n1}')
print('\033[37m Você digitou o valor {}. Seu sucessor é {} e o seu antecessor é {}'.format(n,n2,n1))