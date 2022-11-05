# Librarys
from flask import  request, Blueprint, render_template, redirect, url_for
from flask_login import login_required
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
	
	return render_template('registro.html')

@registers.route("/api/register", methods=['POST'])
def api_register():
	if request.method == 'POST':
		username = request.form['username'] 
		password = request.form['password']
		password = hashlib.sha256(password.encode('utf-8')).hexdigest()
		rol = "cliente"
		data = qUser.registerUser(username,password,rol)

		return redirect(url_for('login'))
