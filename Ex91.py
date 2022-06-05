from time import sleep
from random import randint
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
print('valores sorteados')
for k, v in jogo.items():
    print(f'{k} tirou {v}')
    sleep(0.5)
ranking = list()#MESMO QUE COLOCASSE COMO DICIONARIO, TRANSFOMARIA EM LISTA
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)#AQUI TRANSFORMA EM LISTA
for i, v in enumerate(ranking):#USA ENUMERATE PQ TRANSFORMOU EM LISTA
    print(f'{i+1}o lugar: {v[0]} com {v[1]}')#v[0] são os nomes e v[1] são os valores
    sleep(0.5)
