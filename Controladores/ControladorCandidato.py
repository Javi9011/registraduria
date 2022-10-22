from Modelos.Candidato import Candidato
class ControladorCandidato():
    def __init__(self):
        print("Creando Controlador Candidato")



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
        print("Elimiando candidato con id ", id)
        return True