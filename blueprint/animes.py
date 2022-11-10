# Librarys
from flask import  request, Blueprint, render_template, redirect, url_for, flash, abort
from flask_login import login_required

# Modules
from querys.querysAnime import qAnime # Querys Animes
from blueprint.Funciones import Funciones 

# Init blueprint animes
animes = Blueprint('animesList', __name__, template_folder='app/templates')

# All animes
@animes.route("/animes")
@login_required
def animesList():
	data = qAnime.fetchall_anime()
	return render_template("series.html", 
		datas = data, 
		titlePage = "Animes - Biblioteca",
		title = "Lista de Animes",
		serie = "anime",
		th = "Cantidad de Temporadas",
		case = 'Temporadas',
		addForm = "Anime")


# Search animes
@animes.route("/anime" , methods=['POST'])
@login_required
def anime():
	if request.method == 'POST':
		search = request.form['search']
		data = qAnime.fetchall_anime()
		dataFilter = Funciones.Filter(data, search) # Filter

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

# Add anime
@animes.route("/api/addAnime" , methods=['POST'])
@login_required
def add_anime():
	if request.method == 'POST':
		nombre = request.form['nombre']
		capitulos = int(request.form['capitulos'])
		temporadas = int(request.form['Temporadas'])
		tipoTemp = int(request.form.get('tipo'))
		tipo = ['Japones', 'Coreano', 'Chino']
		tipo = tipo[tipoTemp]
		
		data = qAnime.add_anime(nombre,capitulos,temporadas,tipo)
		if data == True:
			flash('Se ha agregado exitosamente...')
			return	redirect('/animes')
		elif data == False:
			flash('El anime ya existe...')
			return	redirect('/animes')
		else:
			abort(500)
