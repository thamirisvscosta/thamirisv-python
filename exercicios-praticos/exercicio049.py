p = str(input('escreva uma frase: ')).strip().upper()
separa= p.split()
junta = ''.join(separa)
inverso =''
for letra in range(len(junta)-1, -1, -1):
    inverso += junta[letra]
print(f'o inverso de {junta} é {inverso}. ')
if junta ==  inverso:
    print(' logo é um PALÍNDROMO!')
else:
    print('logo NÃO É UM PALÍNDROMO!')
