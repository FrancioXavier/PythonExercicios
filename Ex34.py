sal = float(input('Digite o seu salário aqui: '))
if sal >= 1250:
    ns = sal + (sal*10/100)
    print('Seu aumento é de 10% e seu novo salário é {}'.format(ns))
else:
    ns2 = sal + (sal*15/100)
    print('Seu aumento é de 15% e seu novo salário é {}'.format(ns2))
