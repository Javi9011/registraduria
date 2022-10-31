from Repositorios.InterfaceMesa import RepositorioMesa
from Modelos.Mesa import Mesa

class ControladorMesa():

    def __init__(self):
        print("Creando mesa...")
        self.repositorioMesa = RepositorioMesa()

    def createMesa(self, infoMesa):
        print("Crear mesa...")
        laMesa = Mesa(infoMesa)
        print("Mesa a crear en la Base de Datos: ", laMesa.__dict__)
        self.repositorioMesa.save(laMesa)
        return True

    def buscarTodas(self):
        print("Buscando todas las mesas en la Base de Datos...")
        return self.repositorioMesa.findAll()

    def buscarMesas(self, idObject):
        print("Buscar la mesa", idObject)
        mesa = Mesa(self.repositorioMesa.findById(idObject))
        return mesa.__dict__

    def actualizarMesa(self, mesa):
        mesaActual = Mesa(self.repositorioMesa.findById(mesa["idObject"]))
        print("Actualizando la mesa...", mesaActual)
        mesaActual.numero = mesa["Número mesa"]
        mesaActual.can_ins = mesa["Cantidad inscritos"]
        self.repositorioMesa.save(mesaActual)
        return True

    def borrarMesa(self, id):
        return self.repositorioMesa.delete(id)


