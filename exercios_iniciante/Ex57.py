s = ''
masc = ''
fem = ''
while s != 'M':
    while s != 'F':
        s = str(input('Digite seu sexo: [M/F] ')).upper().strip()[0]
        if s != 'M':
            if s != 'F':
                print('Opção inválida, digite novamente:')
        if s == 'M':
            print('Você é do sexo masculino')
        elif s == 'F':
            print('Você é do sexo feminino')


