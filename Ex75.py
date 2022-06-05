c1 = c2 = c3 = c4 = par = 0
c = 1
while c != 5:
    n = int(input(f'Digite o {c}o valor: '))
    if c == 1:
        c1 = n
    elif c == 2:
        c2 = n
    elif c == 3:
        c3 = n
    elif c == 4:
        c4 = n
    c += 1
tupla = (c1, c2, c3, c4)
print(tupla)
print(f'O numero 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O numero 3 foi digitado pela primeira vez na posição {tupla.index(3)+1}')
else:
    print('O numero 3 não foi digitado')
print('Os numeros pares encontrados foram: ')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')