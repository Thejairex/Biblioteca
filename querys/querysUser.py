from main import mysql

class qUser():

    @classmethod
    def login(self, username, password):
        try:
            cur = mysql.connection.cursor()
            query = "SELECT * FROM usuario WHERE username='{}' ".format(username)
        except Exception as e:
            print(str(e))