import mysql.connector


class ConectaMySQL:

    def __init__(self, host, user, database, password=''):
        self.con = mysql.connector.connect(
        host=f'{host}',
        database=f'{database}',
        user=f'{user}',
        password=f'{password}')

    def comando(self, comand):
        cursor = self.con.cursor()
        cursor.execute(f'{comand};')
        for x in cursor:
            print(x)
        cursor.close()

    def criar(self, tipo, comando):
        try:
            create = f'''{comando}'''
            cursor = self.con.cursor()
            cursor.execute(create)
            print(f'{tipo} criado(a) com sucesso!')
            cursor.close()
        except mysql.connector.Error as erro:
            print(f'Falha ao criar {tipo} mysql: {erro}')

    def close(self):
        if self.con.is_connected():
            self.con.close()
            print('Sistema fechado')
        else:
            print('Sistema já está fechado')






