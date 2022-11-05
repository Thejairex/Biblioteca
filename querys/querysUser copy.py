from main import mysql
from flask_login import UserMixin
import time
from User import User

class qUser(UserMixin):

    @classmethod
    def findUser(self, username):
            try:
                cur = mysql.connection.cursor()
                query = "SELECT * FROM usuario WHERE username='{}' ".format(username)
                cur.execute(query)
                data = cur.fetchone()
                return data
                
            except Exception as e:
                print(str(e))
        
    @classmethod
    def getUserID(self, id):
            try:
                cur = mysql.connection.cursor()
                query = "SELECT id, username, role FROM usuario WHERE id={} ".format(id)
                cur.execute(query)
                data = cur.fetchone()
                return data
                
            except Exception as e:
                print(str(e))

    @classmethod
    def loginUser(self, username,password):
        userTemp = self.findUser(username)
        if userTemp != None:
            try:
                cur = mysql.connection.cursor()
                query = "SELECT * FROM usuario WHERE username='{}' AND contraseña='{}'".format(username, password)
                cur.execute(query)
                data = cur.fetchone()
                if data == None:
                    "Contraseña Incorrecta"

                else:
                    print("LOgeado")
                    return data
            except Exception as e:
                print(str(e))
        else:
            return "El usuario no esta regitrado"

    @classmethod
    def registerUser(self, username, password, rol):
        try:
            userTemp = self.findUser(username)
            if userTemp != None:
                return "Ya existe una cuenta con ese nombre de usuario."
            else:
                cur = mysql.connection.cursor()
                query = "INSERT INTO usuario(username,contraseña,rol) VALUES('{}','{}','{}')".format(
                    username, password, rol
                )
                cur.execute(query)
                mysql.connection.commit()
                time.sleep(2.4)
                return self.loginUser(username, password)
        except Exception as e:
            print(e)