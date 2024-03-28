import mysql.connector
from mysql.connector import Error

import os
from dotenv import load_dotenv

load_dotenv()

while True:
    id = input('ID da pessoa: ')
    nome = input('Nome da pessoa: ')

    dados = id + ', \'' + nome + '\')'                                                                                   #\' significa que a aspa faz parte da mensagem

    try:
        con = mysql.connector.connect(
                host='localhost',
                database='cadastro',
                user='root',
                password=os.getenv('PASSWORD'))

        inserirSQL = f"""INSERT INTO besteira (id, nome) 
                        VALUES ({dados}"""
        cursor = con.cursor()
        cursor.execute(inserirSQL)
        con.commit()
        print(f'Número total de registros: {cursor.rowcount}')
        cursor.close()

    except Error as e:
        print(f'Erro ao inserir dados mysql {e}')

    finally:
        resp = str(input('Quer adicionar mais dados? [S/N]')).upper().strip()[0]
        if resp == 'N':
            if con.is_connected():
                con.close()
                cursor.close()
                print('Conexão encerrada')
            break
