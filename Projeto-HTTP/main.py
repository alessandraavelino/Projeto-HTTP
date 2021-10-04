from flask import Flask, render_template, request
from json import dumps

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return dumps(request.form)
    return render_template("index.html")

if __name__== "__main__":
    app.run(debug=True)