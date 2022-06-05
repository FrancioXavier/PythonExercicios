s = c = 0
while True:
    n = int(input('Digite o valor: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'A soma dos {c} valores digitados é {s}')
print('Acabou')
