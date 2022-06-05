pt = int(input('Digite o primeiro termo da progressão: '))
r = int(input('Digite a razão da progressão: '))
pa = pt
res = ''
s = 10
print(pa, end='->')
cont = 1
while cont != 10:
    pa += r
    print(pa, end='->')
    cont += 1
while res != 'N':
    res = str(input('\nVocê quer continuar a progressão? [S/N] ')).upper().strip()
    if res == 'S':
        mpa = int(input('Digite até onde você quer continuar: '))
        mpa2 = cont + mpa
        s = mpa2
        while cont != mpa2:
            pa += r
            print(pa, end='->')
            cont += 1
print('Cabou')
print('Foram feitos {} termos da PA'.format(s))
