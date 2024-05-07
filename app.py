# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/game')
def game():
    # Logic for starting a new game and rendering the Monopoly game page
    return render_template('game.html')

if __name__ == '__main__':
    app.run(debug=True)
