from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/dash")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=8712)
    app.run(debug = True)