s = c = menor = cont = 0
menorn = ''
while True:
    nome = str(input('Digite o nome do produto: '))
    p = float(input('Digite o preço do produto: R$'))
    s += p
    cont += 1
    if cont == 1:
        menorn = nome
        menor = p
    if p >= 1000:
       c += 1
    if p < menor:
        menorn = nome
    sn = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if sn == 'N':
        break
    while sn != 'S':
        sn = str(input('Quer continuar? [S/N]')).upper().strip()[0]
print(f'''O nome do produto mais barato é {menorn}
foram registrados {c} produtos com preço acima de 1000R$
A soma dos preços foi {s}''')
