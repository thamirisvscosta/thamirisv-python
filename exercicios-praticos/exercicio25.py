n = int(input('digite a velocidade do carro: '))
if n <= 80:
    print (f'Muito bom! Sua velocidade é de {n} km/h. Pode continuar sua viagem! :)')
elif n > 80:
    print('Sua velocidade é de {} km/h e está acima da permitida. Você foi multado em R$ 7,00. '.format(n))