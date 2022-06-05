v = float(input('Digite o valor da casa: '))
sal = float(input('Digite o seu salário: '))
t = int(input('Digite o tempo de pagamento em anos: '))
pres = v/(t*12)
if pres <= (sal*30/100):
    print('Empréstimo aceito! as prestação é {:.2f}R$'.format(pres))
else:
    print('Empréstimo negado.')
