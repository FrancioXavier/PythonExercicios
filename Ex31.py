d = int(input('Digite a distância da viagem em quilômetros: '))
if d <= 200:
    p = d*0.5
    print('O preço da sua viagem é´: {}'.format(p))
else:
    p2 = 100 + ((d - 200)*0.45)
    print('O preço da sua viagem é: {}'.format(p2))
