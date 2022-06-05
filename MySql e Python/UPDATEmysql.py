import mysql.connector
from mysql.connector import Error
from MySQLcomandos import ConectaMySQL


def conecta():                                                                                                           #função para conectar com o banco de dados
    try:
        global con
        con = mysql.connector.connect(
            host='localhost',
            database='cadastro',
            user='root',
            password='FdevPy-2708')

    except Error as erro:
        print(f'Erro ao conectar no sistema: {erro}')


def consulta(idhum):                                                                                                     #função para consultar os dados da identificação escolhida
    try:
        conecta()
        consul = f"select * from humano where id = {idhum};"
        cursor = con.cursor()
        cursor.execute(consul)
        linhas = cursor.fetchall()                                                                                       #lê todos as linhas de uma vez só
        for linha in linhas:
            print(f'''
código.......: {linha[0]}
Id...........: {linha[1]}
nome.........: {linha[2]}
profissão....: {linha[3]}
nascimento...: {linha[4]}
sexo.........: {linha[5]}
peso.........: {linha[6]}
altura.......: {linha[7]}
nacionalidade: {linha[8]}''')
    except Error as erro:
        print(f'Erro ao consultar o sistema: {erro}')

    finally:
        if con.is_connected():
            cursor.close()
            con.close()


def atualiza(declara):                                                                                                   #função que atualiza o banco de dados
    try:
        conecta()
        altera = declara
        cursor = con.cursor()
        cursor.execute(altera)
        con.commit()
        print('dado alterado com sucesso!')
    except Error as erro:
        print(f'Falha ao atualizar tabela: {erro}')
    finally:
        if con.is_connected():
            cursor.close()
            con.close()


if __name__ == '__main__':#MAGICAL
    print('ATUALIZAÇÃO DE DADOS NO BANCO MYSQL')
    print('Digite os dados conforme solicitado')
    while True:
        global perg
        idhum = input('Digite o id da pessoa que quer alterar o dado: ')
        consulta(idhum)
        resp = str(input('QUER ALTERAR O DADO DESSA PESSOA? [S//N]')).upper().strip()[0]
        if resp == 'N':
            perg = str(input('QUER CONTINUAR? [S//N]')).upper().strip()[0]
            if perg == 'N':
                break
        elif resp == 'S':
            break
    if resp == 'N':
        pass
    else:
        dado = input('Digite o dado que quer mudar (nome, peso, sexo e etc): ')
        id = input('Digite o id do dado: ')
        att = input('Digite o novo valor: ')
        declara = f'update humano set {dado} = \'{att}\' where id = {id}'
        atualiza(declara)
