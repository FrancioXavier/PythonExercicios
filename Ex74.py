import random
tupla = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))
t = sorted(tupla)
print(sorted(tupla))
print('+'*30)
print(f'O menor valor escolhido foi {t[0]}')
print('+'*30)
print(f'O maior valor escolhido foi {t[4]}')
print('+'*30)

