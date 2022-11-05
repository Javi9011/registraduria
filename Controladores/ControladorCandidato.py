from Repositorios.RepositorioCandidato import  RepositorioCandidato
from Repositorios.InterfacePartido import InterfacePartido
from Modelos.Candidato import Candidato
from Modelos.Partido import Partido
class ControladorCandidato():
    def __init__(self):
        print("Creando Controlador Candidato")
        self.repositorioCandidato=RepositorioCandidato()
        self.repositorioPartido=InterfacePartido()

    def crearCandidato(self, bodyRequest):
        print("creando candidato...")
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

    def actualizarCandidato(self,id,elCandidato):
        candidatoActual=Candidato(self.repositorioCandidato.findById(id))
        candidatoActual.cedula = elCandidato["cedula"]
        candidatoActual.nombre = elCandidato["nombre"]
        candidatoActual.apellido = elCandidato["apellido"]
        self.repositorioCandidato.save(candidatoActual)
        return True

    def deleteCandidato(self, id):
        return self.repositorioCandidato.delete(id)

    def asignarPartido(self,idCandidato,idPartido):
        partidoActual=Partido(self.repositorioPartido.findById(idPartido))
        candidatoActual=Candidato(self.repositorioCandidato.findById(idCandidato))
        print("Partido encontrado: ",partidoActual)
        print("Candidato encontrado: ",candidatoActual)
        candidatoActual.partido=partidoActual
        print("Candidato actualizado: ", candidatoActual)
        return self.repositorioCandidato.save(candidatoActual)
