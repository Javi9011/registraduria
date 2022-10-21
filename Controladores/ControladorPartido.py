from Modelos.Partido import Partido

class ControladorPartido():
    def __int__(self):
        print("Creando controlador de Partido")

    def index(self):
        print("Listar todos los Partidos")
        unPartido = {
            "id": "321",
            "nombre": "fuerza ciudadana",
            "lema": "juntos por un mejor futuro"
        }
        return [unPartido]

    def create(self,infoPartido):
        print("crear un Partido")
        elPartido = Partido(infoPartido)
        return elPartido.__dict__

    def show(self,id):
        print("Mostrando un Partido con su numero de id",id)
        elPartido={
            "id": id,
            "nombre": "fuerza ciudadana",
            "lema": "juntos por un mejor futuro"

        }
        return elPartido

    def update(self,id,infoPartido):
        print("Actualizando un Partido con su numero de id",id)
        elPartido= Partido(infoPartido)
        return elPartido.__dict__

    def delete(self,id):
        print("Eliminado un candidato con su numero id",id)
        return{"delete_count": 1}
