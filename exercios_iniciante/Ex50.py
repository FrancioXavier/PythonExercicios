s = 0
for c in range(1, 7):
    n = int(input('Digite o {}o valor: '.format(c)))
    if n % 2 == 0:
        s += n
print('A soma dos valores pares digitados são: {}'.format(s))
