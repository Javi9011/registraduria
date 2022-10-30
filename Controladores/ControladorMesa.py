from Repositorios.InterfaceMesa import RepositorioMesa
from Modelos.Mesa import Mesa

class ControladorMesa():

    def __init__(self):
        print("Creando mesa...")
        self.repositorioMesa = RepositorioMesa()
    def createMesa(self, infoMesa):
        print("Crear mesa..")
        laMesa = Mesa(infoMesa)
        print("Mesa a crear en la Base de Datos: ", laMesa.__dict__)
        self.repositorioMesa.save(laMesa)
        return True

    def buscarMesas(self):
        print("Listar todas las mesas")
        laMesa = {
            "_id":"abc123",
            "nombre":"Nelson",
            "apellido": "Amaya"
        }
    def buscarporID(self,id):
        print("Mostrando mesa con id",id)
        laMesa = {
            "_id":id,
            "cedula":"123",
            "nombre":"Nelson",
            "apellido":"Amaya"
        }
    def actualizarMesa(self,id,infoMesa):
        print("Actualizando mesa con id",id)
        laMesa = Mesa(infoMesa)
        return laMesa.__dict__
    def borrarMesa(self,id):
        print("Eliminando mesa con id",id)
        return {"deleted_count":1}

