t = str(input('\033[36m Qual temperatura deseja converter? (C,F,K)'))
v = str(input('Para qual? (C,F,K)'))
if t == 'K' and v == 'C':
    k = float(input('digite o valor da temperatura em Kelvin: '))
    c = k - 273
    print(f'O valor em Celsius é {c:.1f} ºC . O valor em Kelvin pedido foi {k:.1f} K.')
else:
    if t == 'K' and v == 'F':
        k = float(input('digite o valor da temperatura em Kelvin: '))
        f = (9*((k-273)/5)) + 32
        print(f'o valor em Farenheit é {f:.1f} ºF. O valor em Kelvin pedido foi {k:.1f} K')
    else:
        if t == 'C' and v == 'K':
            c = float(input('digite o valor da temperatura em Celsius: '))
            k = c + 273
            print(f'\033[31m O valor da temperatura em Kelvin é {k:.1f} K. '
                  f'O valor de Celsius sugerido foi {c:.1f} ºC. ')
        else:
            if t == 'C' and v == 'F':
                c = float(input('\033[35m digite o valor da temperatura em Celsius: '))
                f = ((c/5) * 9) + 32
                print(f'\033[33m O valor da temperatura em Farenheit é {f:.1f} ºF. '
                      f'O valor de Celsius sugerido foi {c:.1f} ºC.')
            else:
                if t == 'F' and v == 'C':
                    f = float(input('Digite o valor da temperatura em Farenheit: '))
                    c = ((f-32) / 9) * 5
                    print(f'O valor da temperatura em Celsius é {c:.1F} ºC. '
                          f'O valor de Farenheint sugerido foi {f:.1F} ºF. ')
                else:
                    if t == 'F' and v == 'K':
                        f = float(input('digite o valor da temperatura em Farenheint: '))
                        k = ((((f-32)/9) * 5) + 273)
                        print(f'O valor da temperatura em Kelvin é {k:.1f} K. '
                              f'O valor em Farenheint sugerido foi {f:.1f} ºF.')
                    else:
                        print('Temperatura desconhecida. Tente novamente!')
print('fim!')
