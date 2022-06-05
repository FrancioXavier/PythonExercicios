def notas(*n, sit=False):
    """
    -> Função para analisar notas de vários alunos.
    :param n: serve para adicionar as notas à função
    :return: retorna um dicionário com os dados de maior, menor, média e total de notas
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] < 6:
            r['situação'] = 'RUIM'
        elif r['média'] >= 7:
            r['situação'] = 'BOA'
        else:
            r['situação'] = 'RAZOÁVEL'
    return r


resp = notas(6.0, 5.0, 7.0, sit=True)
print(resp)
