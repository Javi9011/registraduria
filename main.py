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

@app.route("/candidato/<string:id>/partidos/<string:id_partido>",methods=['PUT'])
def asignarPartidoACandidato(id,id_partido):
    json=ControladorCandidato.asignarPartido(id,id_partido)
    return jsonify(json)

@app.route("/resultados",methods=['GET'])
def getResultados():
    json=ControladorResultado.index()
    return jsonify(json)
@app.route("/resultados/<string:id>",methods=['GET'])
def getResultado(id):
    json=ControladorResultado.mostrarID()
    return jsonify(json)
@app.route("/resultados/candidato/<string:id_candidato>/mesa/<string:id_mesa>",methods=['POST'])
def crearResultado(id_candidato,id_mesa):
    data = request.get_json()
    json=ControladorResultado.createResult(data,id_candidato,id_mesa)
    return jsonify(json)
@app.route("/resultados/<string:id_resultados>/candidato/<string:id_candidato>/mesa/<string:id_mesa>",methods=['PUT'])
def modificarResultados(id_resultados,id_candidato,id_mesa):
    data = request.get_json()
    json=ControladorResultado.update(id_resultados,data,id_candidato,id_mesa)
    return jsonify(json)
@app.route("/inscripciones/<string:id_inscripcion>",methods=['DELETE'])
def eliminarInscripcion(id_inscripcion):
    json=miControladorInscripcion.delete(id_inscripcion)
    return jsonify(json)


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])