from main import mysql
from flask_login import UserMixin
import time
from querys.entities.User import User

class qUser(UserMixin):

    # @classmethod
    # def findUser(self, username):
    #         try:
    #             cur = mysql.connection.cursor()
    #             query = "SELECT * FROM usuario WHERE username='{}' ".format(username)
    #             cur.execute(query)
    #             data = cur.fetchone()
    #             return data
                
    #         except Exception as e:
    #             raise e
        
    @classmethod
    def getUserID(self, id):
            try:
                cur = mysql.connection.cursor()
                query = "SELECT id, username, rol FROM usuario WHERE id={} ".format(id)
                cur.execute(query)
                data = cur.fetchone()
                if data == None:
                    return None 
                else:
                    user = User(data[0],data[1],None,data[2])
                    return user
            except Exception as e:
                print(e)

    @classmethod
    def loginUser(self, user):
        
        try:
            cur = mysql.connection.cursor()
            query = "SELECT * FROM usuario WHERE username='{}'".format(user.username)
            cur.execute(query)
            data = cur.fetchone()
            if data == None:
                return None
            else:
                if data[2] == user.password:
                    verificatedPassword = True
                else: 
                    verificatedPassword = False
                user = User(data[0],data[1],verificatedPassword,data[3])
                return user
        except Exception as e:
            print(e)
        
    @classmethod
    def registerUser(self, username, password, rol):
        try:
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