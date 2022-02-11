l1 = int(input('Digite o valor da primeira linha: '))
l2 = int(input("Digite o valor da segunda linha: "))
l3 = int(input('Digite op valor da terceira linha: '))
if l1 == l2 == l3:
    print('\033[34m Podem formar um triângulo equilátero!')
elif l1 == l2 and l1 >= l3 and l2 >= l3:  # isosceles
    print('\033[35m Podem formar um triângulo isosceles!')
elif l1 == l3 and l1 >= l2 and l3 >= l2:  # isosceles
    print('\033[35m Podem formar um triângulo isosceles!')
elif l2 == l3 and l2 >= l1 and l3 >= l1:  # isosceles
    print('\033[35m Podem formar um triângulo isosceles!')
elif l1 != l2 != l3:
        print('\033[36m Podem formar um triângulo escaleno!')
