p = float(input('Digite o preço do produto: '))
cond = int(input('''Escolha a forma de pagamento:
[1] à vista (dinheiro ou cheque)
[2] à vista (cartão)
[3] até 2x no cartão
[4] 3x ou mais no cartão
Sua opção: '''))
if cond == 1:
    p2 = p - (p * 10/100)
    print('Valor a pagar: {}'.format(p2))
elif cond == 2:
    p3 = p - (p * 5/100)
    print('Valor a pagar: {}'.format(p3))
elif cond == 3:
    parc = p/2
    print('Valor a pagar: {} \nValor da parcela: {}'.format(p, parc))
elif cond == 4:
    vz = int(input('Digite a quantidade de parcelas: '))
    p4 = p + (p*20/100)
    parc2 = p4/vz
    print('Valor a pagar: {} \nValor da parcela: {}'.format(p4, parc2))
else:
    print('Escolha não validada.')