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


@app.route("/novelas/new")
def new_novel():
    return render_template("add.html", type="Novela")


@app.route("/api/add_Novela", methods=["POST"])
def add_novela():
    types = ["Novela Web JP",
             "Novela Web KR",
             "Novela Web CH",
             "Novela Ligera JP",
             "Novela Ligera KR",
             "Novela Ligera CH"]
    
    status = ["Finalizado", "En Lectura" , "En Hiatus", "Sin Empezar"]

    name = str(request.form["name"])
    type = int(request.form["type"])
    type = types[type-1]
    state = int(request.form["status"])
    state = status[state-1]
    score = float(request.form["score"])
    favorite = int(request.form["favorite"])

    return f"nombre: {name}, tipo: {type}, status: {state}, score: {score}, favorito: {favorite}"


if __name__ == "__main__":
    app.run(debug=True)
