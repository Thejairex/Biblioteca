# Module Funciones
class Filter():

    # Filter system
    @classmethod
    def Filter(self, data, search):
        dataFilter = []
        for i in data:
            if search.upper() in i[1].upper():
                dataFilter.append(i)

        return dataFilter

