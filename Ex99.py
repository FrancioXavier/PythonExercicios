valores = []


def maior(*num):
    valores.sort(reverse=True)
    print('>>'*25)
    print(f'O maior valor digitado foi {valores[0]} de {len(valores)} valores digitados')
    print('>>' * 25)


while True:
    print('--'*20)
    valores.append(int(input('Digite o valor para adicionar à lista: ')))
    print('--' * 20)
    p = str(input('Quer continuar? [S/N] '))
    if p in "nN":
        break
    print('--' * 20)
maior(valores)
