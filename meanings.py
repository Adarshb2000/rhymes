import sqlite3

conn = sqlite3.connect('database/rhymes.db')
db = conn.cursor()

with conn:
    db.execute("CREATE TABLE Meanings (word varchar(200) PRIMARY KEY UNIQUE NOT NULL, meaning text)")
    # db.execute("DROP TABLE Meanings")
    pass

# print(db.execute("SELECT * FROM Meanings").fetchall())
