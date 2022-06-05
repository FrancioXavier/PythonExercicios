menor = maior = pos = posm = 0
lista = []
for c in range(0, 5):#como ja sabe o começo e o fim pode usar for
    lista.append(int(input('Digite o valor para adicionar à lista: ')))#append pra adicionar à lista
    if c == 0:#definir valores para poder trocar ou não depois
        menor = lista[0]
        maior = lista[0]
    elif lista[c] < menor:
        menor = lista[c]
        pos = c
    elif lista[c] > maior:
        maior = lista[c]
        posm = c
print(f'''a lista: {lista}
O maior valor imposto à lista foi {maior} na posição {posm} 
O menor valor foi {menor} na posição {pos}''')

