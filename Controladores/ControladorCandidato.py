from Modelos.Candidato import Candidato
class ControladorCandidato():
    def __init__(self):
        print("Creando Controlador Candidato")

    def crearCandidato(self, infoCandidato):
        print("crear candidato")
        elCandidato = Candidato(infoCandidato)
        return elCandidato.__dict__

    def buscarTodos(self):
        print("Listar candidatos")
        return True

    def buscarCandidato(self,id):
        print("Buscando el candidato... ", id)
        return True

    def updateCandidato(self, id, elCandidato):
        print("Actualizando candidato con id ", id)
        return True

    def deleteCandidato(self, id):
        print("Borrar candidato con id ", id)
        return True