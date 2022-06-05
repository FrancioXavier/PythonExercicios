m = []
m0 = []
m1 = []
m2 = []
sp = 0
for c in range(0, 3):
    m0.append(int(input(f'Digite a coordenada 0,{c}: ')))
    if m0[c] % 2 == 0:
        sp += m0[c]
for c in range(0, 3):
    m1.append(int(input(f'Digite a coordenada 1,{c}: ')))
    if m1[c] % 2 == 0:
        sp += m1[c]
for c in range(0, 3):
    m2.append(int(input(f'Digite a coordenada 2,{c}: ')))
    if m2[c] % 2 == 0:
        sp += m2[c]
m.append(m0.copy())
m.append(m1.copy())
m.append(m2.copy())
maior = m1[0]
if m1[1] > maior:
    maior = m1[1]
if m1[2] > maior:
    maior = m1[2]
print(f'[{m[0][0]:^5}] [{m[0][1]:^5}] [{m[0][2]:^5}]')
print(f'[{m[1][0]:^5}] [{m[1][1]:^5}] [{m[1][2]:^5}]')
print(f'[{m[2][0]:^5}] [{m[2][1]:^5}] [{m[2][2]:^5}]')
print(f'O maior número da segunda linha é {maior}')
print(f'A soma dos valores da terceira coluna é {m[0][2] + m[1][2] + m[2][2]}')
print(f'A soma dos valores pares da matriz é {sp}')
