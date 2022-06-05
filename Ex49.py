print('~='*20)
print('Tabuada')
print('~='*20)
tab = int(input('Digite um número que queira saber a tabuada: '))
for c in range(1, 11):
    r = tab * c
    print('O resultado de {} x {} é {}'.format(tab, c, r))
