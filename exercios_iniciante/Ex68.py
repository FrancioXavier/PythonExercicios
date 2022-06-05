import random
cont = 0
while True:
    escolha = random.randint(0, 11)
    pi = ['par', 'impar']
    escolha2 = random.choice(pi)
    j = int(input(f'VAMOS BRINCAR! Eu escolhi {escolha2}, digite um número e vamos ver se você ganha de mim: '))
    if (j + escolha) % 2 == 0:
        if escolha2 == 'impar':
            cont += 1
            print(f'Eu escolhi {escolha} e você {j}, eu perdi, vamos de novo!')
    elif (j + escolha) % 2 != 0:
        if escolha2 == 'par':
            cont += 1
            print(f'Eu escolhi {escolha} e você {j}, eu perdi, vamos de novo!')
    if (j + escolha) % 2 == 0 and escolha2 == 'par':
        print(f'Eu escolhi {escolha} e você {j}, eu ganhei!!!')
        break
    elif (j + escolha) % 2 != 0 and escolha2 == 'impar':
        print(f'Eu escolhi {escolha} e você {j}, eu ganhei!!!')
        break
print(f'ACABOU, você venceu {cont} vezes')
