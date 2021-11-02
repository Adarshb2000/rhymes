import sqlite3

conn = sqlite3.connect('database/rhymes.db')
db = conn.cursor()

# default_value = 'ISAIASSAISIAASIAIS'

with conn:
    # db.execute("CREATE TABLE RhymingWords (id INTEGER PRIMARY KEY UNIQUE NOT NULL DEFAULT 0)"); db.execute("INSERT INTO RhymingWords (id) VALUES ('0')")
    # db.execute("DROP TABLE RhymingWords")
    # db.execute(f"ALTER TABLE RhymingWords ADD COLUMN 'aya' varchar(100) DEFAULT '' ")
    pass


# print(db.execute("PRAGMA table_info('RhymingWords')").fetchall())

# 
# conn.commit()
#db.execute("SELECT id FROM RhymingWords WHERE ")

# print(db.execute("SELECT id FROM RhymingWords WHERE aya = '' LIMIT 1").fetchone())

print(db.execute("SELECT * FROM RhymingWords").fetchall())