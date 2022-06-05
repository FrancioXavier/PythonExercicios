def ajuda(fun):
    if fun != 'fim':
        aj = help(fun)


def titulo(msg):
    print('\033[7:36m~'*len(msg))
    print(msg)
    print('~'*len(msg))


while True:
    titulo('AJUDA PYHELP')
    r = ajuda(str(input('\033[mDigite a função ou biblioteca > \033[7m')).lower().strip())
    p = str(input('\033[mQuer continuar? [S/N]'))
    if p in 'Nn':
        print('\033[1:30:41mATÉ LOGO')
        break
