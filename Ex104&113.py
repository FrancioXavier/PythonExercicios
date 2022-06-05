def leiaint(inp):
    while True:
            try:
                num = int(input(inp))
            except (ValueError, TypeError):
                print('\033[31mERRO! Tipo de dados errado, tente novamente.\033[m')
                continue
            except (KeyboardInterrupt):
                print('\033[31mERRO! Entrada de dados interrompida pelo usuário\033[m')
                return 0
            else:
                return num


def leiafloat(num):
    while True:
        try:
            v = float(input(num))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número real válido\033[m')
            continue
        else:
            return v


n = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o número {n}')
f = leiafloat('Digite um número real: ')
print(f'Você acabou de digitar {f}')
print('VOLTE SEMPRE')
