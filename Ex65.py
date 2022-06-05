r = ''
c = maior = menor = s = 0
while r != 'N':
    n = int(input('Digite um valor: '))
    if c == 0:
        maior = n
        menor = n
    s += n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    c += 1
    r = str(input('Você deseja continuar? [S/N]')).upper().strip()
m = s/c
print('''A soma dos valores é {}
a média dos valores é {}
o maior valor digitado foi {}
o menor valor digitado foi {}'''.format(s, m, maior, menor))
