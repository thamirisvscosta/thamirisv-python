# IMC
p = float(input('Qual é o seu peso?  '))
h = float(input('Qual é sua altura?  '))
imc = p / (h ** 2)
if imc < 18.5:
    print(f'Seu imc é de {imc:.2f}, ou seja, você está abaixo do seu peso. ')
elif 18.5 < imc < 25:
    print(f'Seu imc é de {imc:.2f}, ou seja, você está no seu peso ideal. ')
elif 25 < imc < 30:
    print(f'Seu imc é de {imc:.2f}, ou seja, você está com sobrepeso. ')
elif 30 < imc < 40:
    print(f'Seu imc é de {imc:.2f}, ou seja, você está com obesidade. ')
elif imc > 40:
    print(f'Seu imc é de {imc:.2f}, ou seja, você está com obesidade mórbita. ')
