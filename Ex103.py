def ficha(nome='Nome não informado', gols=0):
    print('~='*10)
    print('FICHA DO JOGADOR')
    print('~='*10)
    print(f'NOME: {nome}')
    print(f'GOLS TOTAIS: {gols}')


dados = ficha(nome=str(input('Digite o nome do jogador: ')), gols=int(input('Quantidade de gols totais: ')))
