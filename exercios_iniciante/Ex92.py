import datetime
ct = {}
ct['nome'] = str(input('Digite seu nome: '))
i = int(input('Digite seu ano de nascimento: '))
ct['idade'] = datetime.date.today().year - i
cart = int(input('Digite sua carteira de trabalho: '))
ct['ctps'] = cart
if cart != 0:
    con = int(input('Digite seu ano de contratação: '))
    ct['contratação'] = con
    ct['salário'] = float(input('Digite seu salário: '))
    tr = 35 - (datetime.date.today().year - con)
    ct['aposentadoria'] = tr + (datetime.date.today().year - i)
for k, v in ct.items():
    print(f'{k} = {v}')

