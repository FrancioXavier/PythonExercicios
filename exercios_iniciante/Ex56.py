Si = 0
Mih = 0
im = 0
Nh = ''
Mi = 0
for c in range(1, 5):
    print('~='*10)
    print('{}ª pessoa'.format(c))
    print('~='*10)
    n = str(input('Nome: '))
    i = int(input('Idade: '))
    s = str(input('Digite seu sexo [M/F/O]: '))
    
    Si += i
    if c == 1 and s in 'Mm':
        Mih = i
        Nh = n
    if s in 'Mm' and i > Mih:
        Mih = i
        Nh = n
    if s in 'Ff' and i < 20:
        im += 1
Mi = Si/4
print('A média de idade é: {}'.format(Mi))
print('O homem mais velho se chama {} e tem {} anos'.format(Nh, Mih))
print('Tem {} mulheres com menos de 20 anos'.format(im))

