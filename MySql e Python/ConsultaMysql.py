import mysql.connector
from mysql.connector import Error

import os
from dotenv import load_dotenv

load_dotenv()

try:
    con = mysql.connector.connect(
            host='localhost',
            database='cadastro',
            user='root',
            password= os.getenv('PASSWORD'))

    consultaSQL = "select * from besteira"
    cursor = con.cursor()
    cursor.execute(consultaSQL)
    linhas = cursor.fetchall()
    print(f'Número total de registros: {cursor.rowcount}')

    print('\n Humanos cadastrados')
    for linha in linhas:
        print('~='*20)
        print(f'Id................: {linha[0]}')
        print(f'nome..............: {linha[1]}')
        print(f'{"~=" * 20}\n')

except Error as e:
    print(f'Erro ao acessar tabela mysql {e}')

finally:
    if con.is_connected():
        con.close()
        cursor.close()
        print('Conexão encerrada')
