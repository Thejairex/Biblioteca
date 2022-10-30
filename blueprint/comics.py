from flask import  request, Blueprint, render_template

from querys.querysComic import qComcic
from blueprint.Funciones import Filter

comics = Blueprint('comics', __name__, template_folder='app/templates')

@comics.route("/comics")
def comicsList():
	data = qComcic.fetchall_comic()
	return render_template("series.html", 
		datas = data, 
		titlePage = "Comics - Biblioteca",
		title = "Lista de Comics",
		serie = "comic",
		th = "autor")

@comics.route("/comic" , methods=['POST'])
def comic():
	if request.method == 'POST':
		search = request.form['search']
		data = qComcic.fetchall_comic()
		dataFilter = Filter.Filter(data, search)
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
				titlePage = "Comics - Biblioteca",
				title = "{} Resultado".format(len(dataFilter)),
				serie = "comic",
				th = "autor")
