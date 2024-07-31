from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# SQLite database initialization
def init_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')

    # Insert data into the database
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()

    # Redirect to main.html
    return redirect('/main')

# Route for the main page after form submission
@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/electric')
def about():
    return render_template('electric.html')

@app.route('/events')
def contact():
    return render_template('events.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/events')
def events():
    return render_template('events.html')


if __name__ == '__main__':
    app.run(debug=True)
