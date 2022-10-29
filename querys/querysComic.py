import time
from main import mysql

class qComcic():

    @classmethod
    def fetchall_comic(self):
        try:
            cur = mysql.connection.cursor()
            query = "SELECT * FROM comic"
            cur.execute(query)
            data = cur.fetchall()
            return data
        except Exception as e:
            return f"No Recibido {e}"