import sqlite3

conn = sqlite3.connect('database/rhymes.db')
db = conn.cursor()

with conn:
    db.execute("DROP TABLE RhymingWords")
    db.execute("DROP TABLE Meanings")
    db.execute("CREATE TABLE RhymingWords (id INTEGER PRIMARY KEY UNIQUE NOT NULL DEFAULT 0)"); db.execute("INSERT INTO RhymingWords (id) VALUES ('0')")
    db.execute("CREATE TABLE Meanings (word varchar(200) PRIMARY KEY UNIQUE NOT NULL, meaning text)")