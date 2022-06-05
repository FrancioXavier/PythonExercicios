cid = str(input('Digite o nome da sua cidade: ')).strip()
sc = cid.split()
santo = sc[0].upper() == 'SANTO'
print('A sua cidade começa com Santo? \n {}'.format(santo))
