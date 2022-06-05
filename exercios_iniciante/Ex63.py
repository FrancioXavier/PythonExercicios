print('\033[36m~='*20)
print('Sequência de fibonacci')
print('~=\033[m'*20)
t1 = 0
t2 = 1
n = int(input('escolha a quantidade de termos de fibonacci: '))
print(t1, end='>')
print(t2, end='>')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(t3, end='->')
    t1 = t2
    t2 = t3
    cont += 1
print('Fim')

