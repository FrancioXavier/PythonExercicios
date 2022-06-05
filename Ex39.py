from datetime import date
nasc = int(input('Digite seu ano de nascimento: '))
a = date.today().year
idade = a - nasc
if idade < 18:
    saldo = 18 - idade
    ano = a + saldo
    print('Ainda não é hora de se alistar, você se alistará em {}, daqui {} anos'.format(ano, saldo))
elif idade == 18:
    print('Está na hora de se alistar')
else:
    saldo = idade - 18
    ano2 = a - saldo
    print('Seu alistamento foi há {} anos, em {}'.format(saldo, ano2))
