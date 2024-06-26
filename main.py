import sqlite3

conn = sqlite3.connect('banco.db')

cursor = conn.cursor()

cursor.execute("CREATE TABLE usuarios (nome text, email text,senha text,genero text,estado text, cidade text, conheceu text, conhecimento text)")