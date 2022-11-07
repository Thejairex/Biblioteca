# Librarys
from flask import  request, Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
import hashlib

# Modules
from querys.querysAnime import qAnime # Querys Animes
from blueprint.Funciones import Funciones 
from querys.querysUser import qUser

# Init blueprint animes
registers = Blueprint('registers', __name__, template_folder='app/templates')

# Route Register
@registers.route("/register")
@login_required
def register():
	if current_user.rol == 'Administrador':
		return render_template('registro.html',
		titlePage = "Registro",
		title = "Registrar nueva cuenta")
	else:
		return render_template('404.html',
		titlePage = "Not Found") , 404

@registers.route("/api/register", methods=['POST'])
@login_required
def api_register():
	if request.method == 'POST':
		username = request.form['username'] 
		password = request.form['password']
		password = hashlib.sha256(password.encode('utf-8')).hexdigest()
		rolTemp = int(request.form.get('rol'))
		if rolTemp == 1:
			rol = 'Administrador'
		elif rolTemp == 2:
			rol = 'Cliente'

		data = qUser.registerUser(username,password,rol)
		
		return redirect(url_for('registers.register'))
		
