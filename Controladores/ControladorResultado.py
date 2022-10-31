from Repositorios.RepositorioResultado import  RepositorioResultado
from Modelos.Resultado import Resultado


class ControladorResultado():
    def __init__(self):
        print("Creando Controlador Resultado")
        self.repositorioResultado = RepositorioResultado()

    def crearResultado(self, bodyRequest):
        print("crear resultado...")
        elResultado = Resultado(bodyRequest)
        print("Resultados a crear en la Base de Datos: ", elResultado.__dict__)
        self.repositorioResultado.save(elResultado)
        return True

    def buscarTodosResul(self):
        print("Buscando todos los resultados en la Base de Datos...")
        return self.repositorioResultado.findAll()

    def buscarResultado(self, idObject):
        print("Buscando el resultado... ", idObject)
        resultado = Resultado(self.repositorioResultado.findById(idObject))
        return resultado.__dict__

    def actualizarResultado(self, resultado):
        resultadoActual = Resultado(self.repositorioResultado.findById(resultado["idObject"]))
        print("Actualizando el resultado....", resultadoActual)
        resultadoActual.numero_mesa = resultado["nombre"]
        resultadoActual.cedula_candidato = resultado["apellido"]
        resultadoActual.numero_votos = resultado["cedula"]
        self.repositorioResultado.save(resultadoActual)
        return True

    def deleteResultado(self, id):
        return self.repositorioResultado.delete(id)