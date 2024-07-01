import pymysql
import os
import dotenv
import pymysql.cursors

TABLE_NAME = 'customers'

dotenv.load_dotenv()

con = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
with con:
    with con.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT,'
            'nome VARCHAR(50) NOT NULL,'
            'idade INT NOT NULL,'
            'PRIMARY KEY (id)'
            ')'
        )
        con.commit()

    with con.cursor() as cursor:
        sql = (
            #  NORMAL
            # f'INSERT INTO {TABLE_NAME} (nome, idade)'
            # 'VALUES ("João", 18)'

            #  COM PLACEHOLDER
            # f'INSERT INTO {TABLE_NAME} (nome, idade)'
            # 'VALUES (%s, %s)'

            #  COM DICT PLACEHOLDER
            f'INSERT INTO {TABLE_NAME} (nome, idade)'
            'VALUES (%(nome)s, %(idade)s)'
        )
        data = {
            'nome': 'Matheus',
            'idade': 18
        }
        cursor.execute(sql, data)
        con.commit()

    with con.cursor() as cursor:
        sql = (
            #  NORMAL
            # f'INSERT INTO {TABLE_NAME} (nome, idade)'
            # 'VALUES ("João", 18)'

            #  COM PLACEHOLDER
            # f'INSERT INTO {TABLE_NAME} (nome, idade)'
            # 'VALUES (%s, %s)'

            #  COM DICT PLACEHOLDER
            f'INSERT INTO {TABLE_NAME} (nome, idade)'
            'VALUES (%(nome)s, %(idade)s)'
        )
        data2 = [
            {
                'nome': 'Douglas',
                'idade': 15
            },
            {
                'nome': 'Pablo',
                'idade': 14
            },
            {
                'nome': 'Adolf',
                'idade': 45
            },
            {
                'nome': 'Caliban',
                'idade': 69
            },
            {
                'nome': 'Matias',
                'idade': 6
            },
            {
                'nome': 'Godofredo',
                'idade': 18
            }
        ]
        cursor.executemany(sql, data2)
        con.commit()

    with con.cursor() as cursor:
        atributo = "id"
        sql = (
            f'SELECT * FROM {TABLE_NAME} WHERE {atributo} = %s'
        )
        data = 6
        cursor.execute(sql, data)
        # PEGA SOMENTE UM RESULTADO
        # result = cursor.fetchONE()
        result = cursor.fetchall()
        print(result)

    with con.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} WHERE id = %s'
        )
        cursor.execute(sql, 5)
        con.commit()
    with con.cursor() as cursor:
        sql = (
            f'UPDATE {TABLE_NAME} SET nome = %s, idade = %s WHERE id = %s'
        )
        cursor.execute(sql, ('Skibidi', 18, 99))
        con.commit()
