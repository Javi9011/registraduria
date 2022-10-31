from Repositorios.RepositorioCandidato import  RepositorioCandidato
from Modelos.Candidato import Candidato
class ControladorCandidato():
    def __init__(self):
        print("Creando Controlador Candidato")
        self.repositorioCandidato=RepositorioCandidato()

    def crearCandidato(self, bodyRequest):
        print("crear candidato...")
        elCandidato = Candidato(bodyRequest)
        print("Candidato a crear en la Base de Datos: ",elCandidato.__dict__)
        self.repositorioCandidato.save(elCandidato)
        return True

    def buscarTodos(self):
        print("Buscando todos los candidatos en la Base de Datos...")
        return self.repositorioCandidato.findAll()

    def buscarCandidato(self,idObject):
        print("Buscando el candidato... ", idObject)
        candidato = Candidato(self.repositorioCandidato.findById(idObject))
        return candidato.__dict__

    def actualizarCandidato(self, candidato):
        candidatoActual = Candidato(self.repositorioCandidato.findById(candidato["idObject"]))
        print("Actualizando el candidato....", candidatoActual)
        candidatoActual.nombre = candidato["nombre"]
        candidatoActual.apellido = candidato["apellido"]
        candidatoActual.cedula = candidato["cedula"]
        self.repositorioCandidato.save(candidatoActual)
        return True

    def deleteCandidato(self, id):
        return self.repositorioCandidato.delete(id)
