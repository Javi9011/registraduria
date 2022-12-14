from Repositorios.InterfaceResultado import  RepositorioResultado
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.InterfaceMesa import RepositorioMesa
from Modelos.Resultado import Resultado
from Modelos.Candidato import Candidato
from Modelos.Mesa import Mesa
class ControladorResultado():

    def __init__(self):
        print("Creando Controlador Resultado")
        self.repositorioResultado=RepositorioResultado()
        self.repositorioCandidato=RepositorioCandidato()
        self.repositorioMesa=RepositorioMesa()

    def index(self):
        return self.repositorioResultado.findAll()

    """
    Asignacion candidato y mesa a resultado
    """

    def createResult(self,bodyRequest,idCandidato,idMesa):
        nuevoResultado = Resultado(bodyRequest)
        elCandidato = Candidato(self.repositorioCandidato.findById(idCandidato))
        laMesa = Mesa(self.repositorioMesa.findById(idMesa))
        nuevoResultado.candidato = elCandidato
        nuevoResultado.mesa = laMesa
        print("Resultado a crear en BD: ",nuevoResultado.__dict__)
        return self.repositorioResultado.save(nuevoResultado)

    def mostrarID(self, id):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__
    """
    Modificación de inscripción (candidato y mesa)
    """


    def update(self, id, infoResultado, id_mesa, id_candidato):
        nuevoResultado = Resultado(self.repositorioResultado.findById(id))
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        nuevoResultado.mesa = laMesa
        nuevoResultado.candidato = elCandidato
        return self.repositorioResultado.save(nuevoResultado)

    def deleteResult(self, id):
        return self.repositorioResultado.delete(id)
