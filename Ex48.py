S = 0
Cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        S += c
        Cont += 1
print('A soma dos {} numeros multiplos de 3 é: {}'.format(Cont, S))
