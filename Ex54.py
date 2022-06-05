from datetime import date
anoA = date.today().year
s = 0
m = 0
for c in range(1, 8):
    p = int(input('Digite o ano de nascimento da pessoa {}: '.format(c)))
    idade = anoA - p
    if idade >= 21:
        s = s + 1
    else:
        m = m + 1
print('Foram listadas {} menores de idade e {} na maioridade'.format(m, s))
