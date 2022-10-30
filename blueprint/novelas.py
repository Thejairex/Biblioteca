from flask import  request, Blueprint, render_template

from querys.querysNovelas import qNovela
from blueprint.Funciones import Filter


novelas = Blueprint('novelas', __name__, template_folder='app/templates')

@novelas.route("/novelas")
def novelasList():
	data = qNovela.fetchall_novela()
	return render_template("novelas.html", datas=data, titlePage="Novelas - Biblioteca")

@novelas.route("/novela" , methods=['POST'])
def novela():
	if request.method == 'POST':
		search = request.form['search']
		data = qNovela.fetchall_novela()

		dataFilter = Filter.Filter(data, search)

		if len(dataFilter) != 1:
			return render_template("novelas.html", datas=dataFilter,  serie="novela", titulo="Novela", titlePage="Novela - Biblioteca")
		else:
			return render_template("comic.html", datas=dataFilter[0], serie="comic", titulo="Comic", titlePage="Comic - Biblioteca")