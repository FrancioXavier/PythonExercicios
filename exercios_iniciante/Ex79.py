lista = []
c = v = 0
while True:
        n = int(input('Digite um valor para colocar na lista: '))#como tem uma condição usou uma variável pra poder colocar depois
        if n not in lista:#LEMBRAR QUE EXISTE IN!!
            print('Número adicionado com sucesso!')
            lista.append(n)#como atendeu a condição, adicionou à lista
        else:
            print('Número duplicado, tente novamente...')
        r = str(input('Quer continuar? [S/N]')).upper().strip()[0]#não atendeu, voltou
        if r == 'N':
            break

print(lista.sort())
