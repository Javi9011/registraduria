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



@app.route("/candidato/<string:id>", methods=['PUT'])
def actualizarCandidato(id):
    data = request.get_json()
    json = ControladorCandidato.actualizarCandidato(id,data)
    return jsonify(json)

@app.route("/candidato/<string:id>", methods=['DELETE'])
def eliminarCandidato(id):
    result = controladorCandidato.deleteCandidato(id)
    if result is None:
        return {"resultado": "No se elimina el candidato en base de datos!"}
    else:
        return jsonify(result)

#metodos Partido



@app.route("/partidos",methods=['POST'])
def createPartido():
    data= request.get_json()
    json=miControladorPartido.crearPartido(data)
    return jsonify(json)

@app.route("/partidos/<string:id>",methods=['GET'])
def ShowPartido(id):
    result=miControladorPartido.buscarPartido(id)
    if result is None:
        return {"resultado": "No se encuentra el partido en base de datos!"}
    else:
        return jsonify(result)

@app.route("/partidos",methods=['GET'])
def buscarAll():
    result= miControladorPartido.buscarTodosLosPartidos()
    if not result:
        return {"resultado": "No se encuentran los Partidos"}
    else:
        return jsonify(result)

@app.route("/partidos", methods=['PUT'])
def actualizarPartido():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result= miControladorPartido.actualizarPartido(requestBody)
    if result:
        return {"resultado": "Partido actualizado!"}
    else:
        return {"resultado": "Error al actualizar el Partido!"}

@app.route("/partidos/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    result= miControladorPartido.deletePartido(id)
    if result is None:
        return {"resultado": "No se elimina el Partido en base de datos!"}
    else:
        return jsonify(result)

@app.route("/resultados",methods=['POST'])
def crearResultado():
    data = request.get_json()
    json=controladorResultado.crearResultado(data)
    return jsonify(json)
    if result:
        return {"result": "El candidato se creo correctamente"}
    else:
        return {"result": "Error"}

@app.route("/resultados",methods=['GET'])
def buscasResultados():
    result=controladorResultado.buscarTodos()
    if not result:
        return {"resultado": "No se encuentran candidatos"}
    else:
        return jsonify(result)

@app.route("/resultados/<string:id>", methods=['GET'])
def searchResultado(id):
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

@app.route("/resultados/<string:id>", methods=['DELETE'])
def borrarResultado(id):
    result=controladorResultado.deleteResultado(id)
    if result is None:
        return {"resultado":"No se elimino resultado"}
    else:
        return jsonify(result)

#Métodos mesa
@app.route("/mesa", methods=['POST'])
def crearMesa():
    data = request.get_json()
    json = controladorMesa.createMesa(data)
    return jsonify(json)

@app.route("/mesa/<string:id>",methods=['GET'])
def buscarMesa(id):
    result = controladorMesa.buscarMesas(id)
    if result is None:
        return {"resultado": "No se encuentra la mesa en base de datos!"}
    else:
        return jsonify(result)

@app.route("/mesa", methods=['GET'])
def buscarTodas():
    result = controladorMesa.buscarTodas()
    if not result:
        return {"resultado": "No se encuentran mesas"}
    else:
        return jsonify(result)

@app.route("/mesa/<string:id>", methods=['PUT'])
def actualizarMesa(id):
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controladorMesa.actualizarMesa(requestBody, id)
    if result:
        return {"mesa": "La mesa fue actualizada!"}
    else:
        return {"mesa": "Error al actualizar la mesa!"}

@app.route("/mesa/<string:id>", methods=['DELETE'])
def borrarMesa(id):
    result = controladorMesa.borrarMesa(id)
    if result is None:
        return {"resultado": "No se elimina la mesa en base de datos!"}
    else:
        return jsonify(result)


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])