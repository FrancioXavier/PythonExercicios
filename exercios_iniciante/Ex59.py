e = 0
n = 0
n1 = int(input('Digite o primeiro valor: '))
maior = n1
n2 = int(input('Digite o segundo valor: '))
print('\033[36m~=\033[m'*10)
print('\033[36mMENU\033[m')
print('\033[36m~=\033[m'*10)
while e != 6:
    e = int(input('''Escolha sua opção:
    [1] soma
    [2] subtração
    [3] maior
    [4] adicionar novo número
    [5] novos números
    [6] sair
    Digite aqui: '''))
    if e == 1:
        som = n1 + n2
        print('A soma dos valores é {}'.format(som))
        print('~='*20)
    elif e == 2:
        sub = n1 - n2
        print('A subtração dos valores é {}'.format(sub))
        print('~=' * 20)
    elif e == 3:
        if n1 > maior:
            maior = n1
            print('O maior valor digitado foi {}'.format(maior))
            print('~=' * 20)
        if n2 > maior:
            maior = n2
            print('O maior valor digitado foi {}'.format(maior))
            print('~=' * 20)
        elif n > maior:
            maior = n
            print('O maior valor digitado foi {}'.format(maior))
            print('~=' * 20)
    elif e == 4:
        n = int(input('Digite um novo valor: '))
        print('~=' * 20)
    elif e == 5:
        nn1 = int(input('Digite o novo primeiro valor: '))
        nn2 = int(input('Digite o novo segundo valor: '))
        n1 = nn1
        n2 = nn2
        print('~=' * 20)
print('Fim')

