l1 = float(input('Diga o lado 1: '))
l2 = float(input('Diga o lado 2: '))
l3 = float(input('Diga o lado 3: '))
if (l1 + l2) > l3:
    if (l2 + l3) > l1:
        if (l3 + l1) > l2:
            print('Os lados {}, {} e {} podem formar um triangulo!'.format(l1, l2, l3))
            if l1 == l2 == l3:
                print('O triângulo é equilátero')
            elif l1 == l2 != l3 or l2 == l3 != l1 or l1 == l3 != l2:
                print('O triângulo é isósceles')
            elif l1 != l2 != l3:
                print('O triângulo é escaleno')
else:
    print('Os lados descritos não formam um triangulo')

