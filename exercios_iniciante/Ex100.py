from random import randint
from time import sleep
numeros = []
npar = []


def sorteio(*n):
    print('Sorteando valores...', end='')
    for c in range(1, 6):
        n = randint(1, 6)
        if n % 2 == 0:
            npar.append(n)
        numeros.append(n)
        print(f'{n}', end=', ')
        sleep(1)


def somapar(*par):
    sum(npar)


sorteio(numeros)
print(f'\nOs numeros sorteados foram: {numeros}')
somapar(npar)
print(f'A soma dos números {npar} pares é {sum(npar)}')
