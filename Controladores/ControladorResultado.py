from Repositorios.InterfaceResultado import  RepositorioResultado
from Modelos.Resultado import Resultado
class ControladorResultado():

    def __init__(self):
        print("Creando Controlador Resultado")
        self.repositorioResultado=RepositorioResultado()

    def crearResultado(self, bodyRequest):
        print("creando resultado...")
        elResultado = Resultado(bodyRequest)
        print("Resultado a crear en la Base de Datos: ",elResultado.__dict__)
        self.repositorioResultado.save(elResultado)
        return True

    def buscarTodos(self):
        print("Buscando todos los resultados en la Base de Datos...")
        return self.repositorioResultado.findAll()

    def buscarResultado(self,idObject):
        print("Buscando el resultado... ", idObject)
        resultado = Resultado(self.repositorioResultado.findById(idObject))
        return resultado.__dict__

    def actualizarResultado(self,id,elResultado):
        resultadoActual=Resultado(self.repositorioResultado.findById(id))
        resultadoActual.cedula = elResultado["cedula"]
        resultadoActual.nombre = elResultado["nombre"]
        resultadoActual.apellido = elResultado["apellido"]
        self.repositorioResultado.save(resultadoActual)
        return True

    def deleteResultado(self, id):
        return self.repositorioResultado.delete(id)