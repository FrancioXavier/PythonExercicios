lista = []
listapar = []
listaimp = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimp.append(n)
    p = str(input('Quer continuar? [N/S]')).upper().strip()[0]
    if p == 'N':
        break
print(f'Números pares: {listapar}')
print(f'Números impares {listaimp}')
print(f'lista: {lista}')
