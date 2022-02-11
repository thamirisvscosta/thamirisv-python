import random
n1 = str(input('\033[32m Digite o nome do aluno 1:'))
n2 = str(input('\033[34m Digite o nome do aluno 2:'))
n3 = str(input('\033[35m Digite o nome do aluno 3:'))
n4 = str(input('\033[36m Digite o nome do aluno 4:'))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem dos(as) alunos(as) escolhidos(as) foi:')
print(lista)