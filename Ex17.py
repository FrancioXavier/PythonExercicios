from math import sqrt
adj = float(input('Digite o cateto adjacente: '))
op = float(input('Digite o cateto oposto: '))
h = sqrt((adj**2) + (op**2))
print('A hipotenusa do cateto {} e do cateto {} é {}'.format(adj, op, h))
