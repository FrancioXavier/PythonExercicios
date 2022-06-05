from random import randint
j = []
aux = []
p = int(input('Digite quantos jogos você quer gerar: '))
for c in range(0, p):
    for n in range(0, 6):
        v = randint(1, 61)
        if n == 0:
            aux.append(v)
        elif v not in aux:
            aux.append(v)
    j.append(aux.copy())
    aux.clear()
print(j)


