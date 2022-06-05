lista = []
for c in range(0, 5):
    v = int(input('Digite um valor: '))#variavel pro input não ir direto
    if c == 0 or v > lista[-1]:#primeiro valor adicionado para ter base ou se for um valor maior só vai precisar adicionar
        lista.append(v)
    else:
        pos = 0
        while pos < len(lista):#posição menor que o total de unidades, já que o numero que chegou é menor
            if v <= lista[pos]:#numero menor que o da posição
                lista.insert(pos, v)#inseriu o numero menor
                break
            pos += 1
print(f'lista em ordem crescente: {lista}')
