import sqlite3

from aula181 import DB_FILE, TABLE_NAME

con = sqlite3.connect(DB_FILE)
cursor = con.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME}')

row = cursor.fetchall()

for r in row:
    _id, name, weight = r
    print(_id, name, weight)
