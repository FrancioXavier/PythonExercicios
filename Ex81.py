lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    p = str(input('Quer continuar? [N/S]')).upper().strip()[0]
    if p == 'N':
        break
print(f'foram digitados {len(lista)} valores')
if 5 in lista:
    print(f'O valor 5 foi encontrado na posição {lista.index(5)}')
if 5 not in lista:
    print('O valor 5 não foi encontrado')
lista.sort(reverse=True)
print(lista)
