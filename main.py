from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorResultado import ControladorResultado
from Controladores.ControladorMesa import ControladorMesa

controladorCandidato = ControladorCandidato()
miControladorPartido= ControladorPartido()
controladorResultado = ControladorResultado()
controladorMesa = ControladorMesa()

app=Flask(__name__)
cors = CORS(app)

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)

@app.route("/candidato", methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json = controladorCandidato.crearCandidato(data)
    return jsonify(json)

@app.route("/candidato/<string:id>", methods=['GET'])
def buscarCandidato(id):
    result = controladorCandidato.buscarCandidato(id)
    if result is None:
        return {"resultado": "No se encuentra el candidato en base de datos!"}
    else:
        return jsonify(result)

@app.route("/candidato", methods=['GET'])
def buscarTodos():
    result = controladorCandidato.buscarTodos()
    if not result:
        return {"resultado": "No se encuentran candidatos"}
    else:
        return jsonify(result)



@app.route("/candidato", methods=['PUT'])
def actualizarCandidato():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controladorCandidato.actualizarCandidato(requestBody)
    if result:
        return {"resultado": "Candidato actualizado!"}
    else:
        return {"resultado": "Error al actualizar el candidato!"}

@app.route("/candidato/<string:id>", methods=['DELETE'])
def eliminarCandidato(id):
    result = controladorCandidato.deleteCandidato(id)
    if result is None:
        return {"resultado": "No se elimina el candidato en base de datos!"}
    else:
        return jsonify(result)

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

@app.route("/mesa", methods=['POST'])
def crearMesa():
    data = request.get_json()
    json = controladorMesa.createMesa(data)
    return jsonify(json)

@app.route("/mesa",methods=['GET'])
def buscarMesas():
    json=ControladorMesa.buscarMesas()
    return jsonify(json)

@app.route("/mesa/<string:id>", methods=['GET'])
def buscarUnaMesa(id):
    result = controladorMesa.buscarporID(id)
    if result is None:
        return {"mesa": "No se encuentra la mesa en base de datos!"}
    else:
        return jsonify(result)

@app.route("/mesa", methods=['PUT'])
def updateMesa():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controladorMesa.actualizarMesa(requestBody)
    if result:
        return {"mesa": "Mesa actualizado!"}
    else:
        return {"mesa": "Error al actualizar la mesa!"}

@app.route("/mesa", methods=['DELETE'])
def deleteMesa():
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