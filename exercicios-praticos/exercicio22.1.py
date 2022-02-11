n1 = str(input('\033[1m digite seu nome completo: ')).strip()
print(n1.upper())
print(n1.lower())
print(len(n1) - n1.count(' '))
print('seu primeiro nome tem {} letras'.format(n1.find(' ')))
# exemplo 2
separa = n1.split()
print('Seu nome é {} e ele tem {} letras '.format(separa[0], len(separa[0])))
# você pode colocar o strip no input do código para remover os vazios diretamente!
# você pode contar quantos espaços tem na palavra e fazer uma operação de subtração para removê-la contra o len!
# E também fazer o código procurar o primeiro espaço que foi no find!'

