# Dupla: Alessandra Avelino // Hacjesse Barbosa

from flask import Flask, render_template, request
from json import dumps

app = Flask(__name__)
agenda = {}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        #return dumps(request.form)
        agenda[ request.form['ID'] ] = request.form
        return render_template("lista.html", agenda = agenda.values())
    return render_template("index.html")


if __name__== "__main__":
    app.run(debug=True)