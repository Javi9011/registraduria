from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorResultado import ControladorResultado

controladorCandidato = ControladorCandidato()
miControladorPartido= ControladorPartido()
controladorResultado = ControladorResultado()

app=Flask(__name__)
cors = CORS(app)

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

#metodos Partido

@app.route("/partidos",methods=['GET'])
def getPartidos():
    json=miControladorPartido.index()
    return jsonify(json)

@app.route("/partidos",methods=['POST'])
def crearPartido():
    data= request.get_json()
    json=miControladorPartido.create(data)
    return jsonify(json)

@app.route("/partidos/<string:id>",methods=['GET'])
def getPartido(id):
    json=miControladorPartido.show(id)
    return jsonify(json)

@app.route("/partidos/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data= request.get_json()
    json=miControladorPartido.update(id)
    return jsonify(json)

@app.route("/partidos/<string:id>",methods=['DELETE'])
def eliminarPartodo():
    json=miControladorPartido.delete(id)
    return jsonify(json)

@app.route("/resultados",methods=['POST'])
def crearResultado():
    data = request.get_json()
    json=controladorResultado.createResultado()
    return jsonify(json)
    if result:
        return {"result": "El candidato se creo correctamente"}
    else:
        return {"result": "Error"}

@app.route("/resultados/<string:id>", methods=['GET'])
def buscarResultado(id):
    result = controladorResultado.buscarResultado(id)
    if result is None:
        return {"resultado": "No se encuentra el candidato en base de datos!"}
    else:
        return jsonify(result)

@app.route("/resultados", methods=['PUT'])
def updateResultado():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controladorResultado.updateResultado(requestBody)
    if result:
        return {"resultado": "Resultado actualizado!"}
    else:
        return {"resultado": "Error al actualizar el Resultado!"}

@app.route("/resultados", methods=['DELETE'])
def deleteResultado():
    requestBody = request.get_json()
    print("Request body: ", requestBody)








def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])