from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
db = "Pizza.db"


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/repent')
def holy_land():
    return "(: the holy land is no longer shaking"


@app.route('/number/<i>/<x>')
def number(i, x):
    return i*int(x)


@app.route('/pizza/<id>')
def test(id):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Pizzas WHERE id = ?", (id,))
    pizza = cur.fetchall()
    return render_template("pizza.html", pizza=pizza)


if __name__ == "__main__":
    app.run(debug=True)
