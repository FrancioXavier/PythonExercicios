v = float(input('Digite a velocidade registrada: '))
if v > 80:
    m = 7*(v - 80)
    print('Carro multado, valor da multa: {}'.format(m))
else:
    print('Carro nas normas de velocidade')
