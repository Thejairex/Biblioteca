from flask import *

from db import Db

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
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
    
    status = ["Completado", "En Emision" , "En Hiatus", "Droppeado"]
    status2 = ["Finalizado", "En Lectura" , "En Hiatus", "Sin Empezar", "Droppeado"]

    name = str(request.form["name"])
    type = int(request.form["type"])
    type = types[type-1]
    state = int(request.form["status"])
    state = status[state-1]
    my_state = int(request.form["my_status"])
    my_state = status2[my_state-1]
    
    score = float(request.form["score"])
    if request.form.get('favorite') == None:
        favorite = 0
    else:
        favorite = request.form["favorite"]
    
    link = str(request.form["link"])
    
    result, reason = db.insert(table="NOVELS", values=(name, type, state, my_state, score, favorite, link))
    if result:
        return redirect(url_for("novelas"))
    else:
        flash(reason)
        return redirect(url_for("new_novel"))


if __name__ == "__main__":
    app.run(debug=True)
