d = float(input('Quantos dias você passou com o carro? '))
km = float(input('Quantos quilômetros rodou? '))
p = (d*60) + (km*0.15)
print(' Você andou com o carro por {}km durante {} dias \n Preço a pagar: {}R$'.format(km, d, p))
