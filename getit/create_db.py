import sqlite3 

con = sqlite3.connect('notes.db')
cur = con.cursor()

sql = '''CREATE TABLE IF NOT EXISTS notes (
    "id"	INTEGER PRIMARY KEY AUTOINCREMENT,
    "titulo" TEXT NOT NULL,
    "detalhes" TEXT NOT NULL
)'''

cur.execute(sql)
con.commit()
con.close()
