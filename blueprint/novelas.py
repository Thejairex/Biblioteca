# Librarys
from flask import  request, Blueprint, render_template

# Modules
from querys.querysNovelas import qNovela # Querys Novelas
from blueprint.Funciones import Filter # Filter System

# Init blueprint novelas
novelas = Blueprint('novelas', __name__, template_folder='app/templates')

# All novelas
@novelas.route("/novelas")
def novelasList():
	data = qNovela.fetchall_novela()
	return render_template("series.html", 
		datas = data, 
		titlePage = "Novelas - Biblioteca",
		title = "Lista de Novelas",
		serie = "novela",
		th = "autor")

# Search novelas
@novelas.route("/novela" , methods=['POST'])
def novela():
	if request.method == 'POST':
		search = request.form['search']
		data = qNovela.fetchall_novela()

		dataFilter = Filter.Filter(data, search) # Filter

		if len(dataFilter) != 1:
			return render_template("series.html", 
				datas = dataFilter, 
				titlePage = "Comics - Biblioteca",
				title = "{} Resultados".format(len(dataFilter)),
				serie = "comic",
				th = "autor")
		else:
			return render_template("search.html", 
				datas=dataFilter[0],
				titlePage = "Novelas - Biblioteca",
				title = "{} Resultado".format(len(dataFilter)),
				serie = "novela",
				th = "autor")