n = int(input('Em qual ano você nasceu ? '))
i = 2021 - n
if i <= 9:
    print(f'Sua categoria é a MIRIM, pois você tem {i} anos de idade.')
elif 9 < i < 14:
    print(f'Sua categoria é a INFANTIL, pois você tem {i} anos de idade.')
elif 14 < i < 19:
    print(f'Sua categoria é a JUNIOR, pois você tem {i} anos de idade.')
elif i == 20:
    print(f'Sua categoria é a SENIOR, pois você tem {i} anos de idade.')
elif i > 20:
    print(f'Sua categoria é a MASTER, pois você tem {i} anos de idade.')