# Module Funciones
from flask_jwt_extended import verify_jwt_in_request
class Funciones():

    # Filter system
    @classmethod
    def Filter(self, data, search):
        dataFilter = []
        for i in data:
            if search.upper() in i[1].upper():
                dataFilter.append(i)

        return dataFilter


    @classmethod
    def verificarToken(self,):
        return verify_jwt_in_request()