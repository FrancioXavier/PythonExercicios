import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(
            host='localhost',
            database='cadastro',
            user='root',
            password='FdevPy-2708')                                                                                      #conexão com o banco de dados

    inserirSQL = """INSERT INTO besteira (id, nome) 
                    VALUES (default, 'Reginaldo'), (default, 'Sérgio'), (default, 'Ronaldo')"""                          #variável para digitar o comando
    cursor = con.cursor()                                                                                                #cursor é responsável por fazer as interações entre com o banco de dados e o python
    cursor.execute(inserirSQL)
    con.commit()                                                                                                         #faz com que a transação seja finalizada e concretizada
    print(f'Número total de registros: {cursor.rowcount}')                                                               #rowcount = contagem de registros
    cursor.close()

except Error as e:
    print(f'Erro ao inserir dados mysql {e}')

finally:
    if con.is_connected():
        con.close()
        cursor.close()
        print('Conexão encerrada')
