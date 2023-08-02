from flask import *

from db import Db

app = Flask(__name__)
db = Db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/novelas")
def novelas():
    datas = db.select_all("NOVELS")
    return render_template("novelas.html", datas=datas)

if __name__ == "__main__":
    app.run(debug=True)