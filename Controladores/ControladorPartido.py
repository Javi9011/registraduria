from Repositorios.InterfacePartido import InterfacePartido
from Modelos.Partido import Partido

class ControladorPartido():
    def __init__(self):
        print("Creando controlador de Partido.....")
        self.repositorioPartido = InterfacePartido()



    def crearPartido(self,bodyRequest):
        print("crear un Partido")
        elPartido = Partido(bodyRequest)
        print("Partido a crear en la base de datos",elPartido.__dict__)
        self.repositorioPartido.save(elPartido)
        return True

    def buscarTodosLosPartidos(self):
        print("Buscando todos los partidos en la Base de Datos...")
        return self.repositorioPartido.findAll()

    def buscarPartido(self,idObject):
        print("buscar partido",idObject)
        partido= Partido(self.repositorioPartido.findById(idObject))
        return partido.__dict__

    def actualizarPartido(self, partido):
        partidoActual = Partido(self.repositorioPartido.findById(partido["idObject"]))
        print("Actualizando Partido",partidoActual)
        partidoActual.id = partido["id"]
        partidoActual.nombre = partido["nombre"]
        partidoActual.lema = partido["lema"]
        self.repositorioPartido.save(partidoActual)
        return True


    def deletePartido(self,id):
        print("Eliminado un Partido con su numero id",id)
        return self.repositorioPartido.delete(id)
