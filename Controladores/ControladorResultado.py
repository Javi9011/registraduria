from Modelos.Resultado import Resultado
class ControladorResultado():

    def __init__(self):
        print("Entró al constructor de la clase Controlador resultado")

    def createResultado(self):
        print("Crear un resultado")
        return True
    def buscarTodos(self):
        print("Listar resultado")
        return True
    def buscarResultado(self,id):
        print("Buscando el resultado... ", id)
        return True
    def updateResultado(self, id):
        print("Actualizando resultado con id ",id)
        return True

    def deleteResultado(self, id):
        return self.repositorioResultado.delete(id)