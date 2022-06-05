from datetime import date
nasc = int(input('Digite seu ano de nascimento: '))
anoA = date.today().year
id = anoA - nasc
if id <= 9:
    print('Você é MIRIM')
elif 9 < id <= 14:
    print('Você é INFANTIL')
elif 14 < id <= 19:
    print('Você é JUNIOR')
else:
    print('Você é SENIOR')