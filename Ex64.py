n = 0
s = 0
v = 0
while n != 999:
    s += n
    n = int(input('Digite um valor [digite 999 para parar]: '))
    if n != 999:
        v += 1
print('A soma dos {} valores digitados é {}'.format(v, s))
