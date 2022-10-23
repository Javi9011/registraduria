from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorResultado import ControladorResultado


app=Flask(__name__)
cors = CORS(app)

controladorCandidato = ControladorCandidato()
controladorResultado=ControladorResultado()

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)


@app.route("/candidato", methods=['POST'])
def crearCandidato():
    requestBody = request.get_json()
    print("body request", requestBody)
    result = controladorCandidato.createCandidato()
    if(result):
        return {"result": "El candidato se creo correctamente"}
    else:
        return {"result": "Error"}

@app.route("/candidato/<string:id>", methods=['GET'])
def buscarCandidato(id):
    result = controladorCandidato.buscarCandidato(id)
    if result is None:
        return {"resultado": "No se encuentra el candidato en base de datos!"}
    else:
        return jsonify(result)

@app.route("/candidato", methods=['PUT'])
def actualizarCandidato():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controladorCandidato.updateCandidato(requestBody)
    if result:
        return {"resultado": "Candidato actualizado!"}
    else:
        return {"resultado": "Error al actualizar el candidato!"}

@app.route("/candidato", methods=['DELETE'])
def eliminarCandidato():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controladorCandidato.deleteCandidato(requestBody)
    if result:
        return {"resultado": "Candidato eliminado!"}
    else:
        return {"resultado": "Error al eliminar el candidato!"}




def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data




if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])
