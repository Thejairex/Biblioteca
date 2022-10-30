from flask import  request, Blueprint, render_template

from querys.querysAnime import qAnime
from blueprint.Funciones import Filter


animes = Blueprint('animes', __name__, template_folder='app/templates')

@animes.route("/animes")
def animesList():
	data = qAnime.fetchall_anime()
	return render_template("series.html", 
		datas = data, 
		titlePage = "Animes - Biblioteca",
		title = "Lista de Animes",
		serie = "anime",
		th = "Cantidad de Temporadas")

@animes.route("/anime" , methods=['POST'])
def anime():
	if request.method == 'POST':
		search = request.form['search']
		data = qAnime.fetchall_anime()
		dataFilter = Filter.Filter(data, search)

		if len(dataFilter) != 1:
			return render_template("series.html", 
				datas = dataFilter, 
				titlePage = "Animes - Biblioteca",
				title = "{} Resultados".format(len(dataFilter)),
				serie = "anime",
				th = "Cantidad de Temporadas")

		else:
			return render_template("search.html", 
				datas=dataFilter[0],
				title = "{} Resultado".format(len(dataFilter)),
				titlePage="Anime - Biblioteca",
				serie = "anime",
				th = "Cantidad de Temporadas")
