import sqlite3

conn = sqlite3.connect('test_sqlite.db')

curs = conn.cursor()

curs.execute('CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')
conn.commit()

curs.execute(
    'INSERT INTO persons(name) values("Mike")'
)
conn.commit()



print("Table created successfully.")

