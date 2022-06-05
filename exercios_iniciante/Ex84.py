cad = []
dado = []
mai = men =  0
while True:
    dado.append(str(input('Digite o nome: ')))
    dado.append(int(input('Digite o peso: ')))
    if len(cad) == 0:
        mai = men = dado[1]
    elif dado[1] > mai:
        mai = dado[1]
    if dado[1] < men:
        men = dado[1]
    cad.append(dado.copy())
    dado.clear()
    pe = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if pe in 'Nn':
        break
print(f'Foram registradas {len(cad)} pessoas')
print(f'O maior peso registrado foi {mai}KG de ', end='')
for c in cad:
    if c[1] == mai:
        print(c[0])
print(f'O menor peso registrado foi {men}KG de ', end='')
for c in cad:
    if c[1] == men:
        print(c[0])
