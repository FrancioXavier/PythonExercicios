peso = float(input('Digite seu peso: '))
alt = float(input('Digite sua altura: '))
imc = peso/(alt**2)
if imc < 18.5:
    print(' Seu imc é {:.1f} \n Você está abaixo do peso.'.format(imc))
elif 18.5 <= imc <= 25:
    print(' Seu imc é {:.1f} \n Você está no peso ideal.'.format(imc))
elif 25 < imc <= 30:
    print(' Seu imc é {:.1f} \n Você está com sobrepeso.'.format(imc))
elif 30 < imc <= 40:
    print(' Seu imc é {:.1f} \n Você está com obesidade.'.format(imc))
else:
    print(' Seu imc é {:.1f} \n Você está com obesidade mórbida'.format(imc))
