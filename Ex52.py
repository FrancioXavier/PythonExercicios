n = int(input('Digite um número: '))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[36m{}\033[m'.format(c), end=' ')
        tot += 1
    else:
        print('\033[31m{}\033[m'.format(c), end=' ')
print('\nO número foi divisivel {} vezes'.format(tot))
if tot == 2:
    print('O número digitado é PRIMO')
else:
    print('O número digitado não é primo')
