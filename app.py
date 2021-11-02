from flask import Flask, render_template, redirect, request
import sqlite3

conn = sqlite3.connect('database/rhymes.db', check_same_thread=False)
db = conn.cursor()

with conn:
    conn.row_factory = lambda cursor, row: str(row[0])
    db_row = conn.cursor()


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_words', methods=['GET', 'POST'])
def add_words():
    if request.method == 'GET':
        return render_template('add_words.html')
    else:
        print(request.form.get('test'))
        ending = request.form.get('ending')
        words = request.form.getlist('word')
        meanings = request.form.getlist('meaning')

        for word, meaning in zip(words, meanings):
            try:
                with conn:
                    db.execute(f"INSERT INTO Meanings (word, meaning) VALUES ('{word}', '{meaning}')")
            except sqlite3.IntegrityError:
                words.remove(word)

        try:
            with conn:
                db.execute(f"ALTER TABLE RhymingWords ADD COLUMN {ending} varchar(100) DEFAULT ''")
        except sqlite3.OperationalError:
            pass

        table_len = len(db.execute("SELECT * FROM RhymingWords").fetchall())
        filled = db.execute(f"SELECT id FROM RhymingWords WHERE {ending} = '' LIMIT 1").fetchone()[0]
        if table_len - filled <= len(words):
            for i in range(table_len, len(words) + filled + 1):
                with conn:
                    db.execute(f"INSERT INTO RhymingWords (id) VALUES ({i})")
            
        
        for index, word in enumerate(words):
            with conn:
                db.execute(f"UPDATE RhymingWords SET {ending} = '{word}' WHERE id = '{filled + index}'")

        

        return redirect('/')

@app.route('/get_words')
def get_words():
    ending = request.args.get('ending')
    rows = db_row.execute(f'SELECT {ending} FROM RhymingWords').fetchall()
    word_meanings = {}
    for row in rows:
        if row == '':
            break
        word_meanings[row] = None
    for word in word_meanings:
        word_meanings[word] = db_row.execute("SELECT meaning FROM Meanings WHERE word = :word", {'word' : word}).fetchone()
    return render_template('words_template.html', word_meanings=word_meanings)



if __name__ == "__main__":
    app.run(debug=True)