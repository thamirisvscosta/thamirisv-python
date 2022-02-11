import random

print('<>'*20)
print('JO KEN PO!!!!!'.center(40))
print('<>'*20)
print(' escolha: pedra, papel, tesoura ')
n = str(input('Qual opção você escolhe?  '))
c = random.choice(['pedra', 'papel', 'tesoura'])
if n == 'pedra' and c == 'papel':
    print(f'\033[31m Você colocou {n} e o computador colocou {c}. Você perdeu! :( ')
else:
    if n == 'pedra' and c == 'tesoura':
        print(f'\033[36m Você colocou {n}  e o computador colocou {c}.Você ganhou! :)')
    else:
        if n == 'papel' and c == 'pedra':
            print(f'\033[36m Você colocou {n} e o computador colocou {c}. Você ganhou! :)')
        else:
            if n == 'papel' and c == 'tesoura':
                print(f'\033[31m Você colocou {n} e o computador colocou {c}.Você perdeu! :(')
            else:
                if n == 'tesoura' and c == 'papel':
                    print(f'\033[36m Você colocou {n} e o computador colocou {c}. Você ganhou! :)')
                else:
                    if n == 'tesoura' and c == 'pedra':
                        print(f'\033[31m Você colocou {n} e o computador colocou {c}.Você perdeu! :(')
                    else:
                        if n == c:
                            print(f'\033[35m Ihh! você colocou {n} e o computador colocou {c} '
                                  f'também...deu empate! '
                                  f'Jogue novamente!')
print('FIM!')

# curso em video resposta
# from random import randint
#from time import sleep
# itens = ('Pedra' , 'Papel', 'Tesoura')
# computador = randint (0,2)
# print( 'escolhas a opções: [0] PEDRA, [1] PAPEL, [2] TESOURA')
# jogador = int(input('Qual é a sua jogada?'))
# print('jo')
# sleep(1)
# print('ken')
# sleep(1)
# print('po')
# print('Computador jogou {}'. format(itens[computador]))
# print('Jogador jogou {}'. format(itens[jogador]))
# o resto é if e elif igual acima!

