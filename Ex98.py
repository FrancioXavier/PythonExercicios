from time import sleep


def contador(inicio, fim, passo):
    print(inicio, end=', ')
    fim2 = 0
    if inicio > fim:
        if passo < 0:
            while fim < inicio:
                inicio += passo
                print(inicio, end=', ', flush=True)
                sleep(0.5)
        elif passo > 0:
            while fim < inicio:
                inicio -= passo
                print(inicio, end=', ', flush=True)
                sleep(0.5)
        elif passo == 0:
            while fim < inicio:
                inicio -= 1
                print(inicio, end=', ', flush=True)
                sleep(0.5)
    if inicio < fim:
        if passo == 0:
            while fim > inicio:
                inicio += 1
                print(inicio, end=', ', flush=True)
                sleep(0.5)
        while fim > inicio:
            inicio += passo
            print(inicio, end=', ', flush=True)
            sleep(0.5)


print('~='*20)
print(f'{"PROGRAMA CONTADOR":^40}')
print('~='*20)
print('Contagem de 1 a 10: ')
contador(1, 10, 1)
print('\nContagem de 10 a 0 diminuindo -2: ')
contador(10, 0, 2)
contador(inicio=int(input('\nDigite o inicio da conta: ')),
         fim=int(input('Digite o fim da conta: ')),
         passo=int(input('Digite o passo: ')))
print('\n~='*20)
