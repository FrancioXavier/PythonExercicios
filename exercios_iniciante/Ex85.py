listap = []
listai = []
listapar = []
for c in range(0, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        listapar.append(n)
    else:
        listai.append(n)
listapar.sort()
listai.sort()
listap.append(listapar)
listap.append(listai)
print(listap)
