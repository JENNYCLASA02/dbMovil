from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.avion import Avion, AvionesSchema

ruta_aviones = Blueprint("ruta_avion", __name__)

avion_schema = AvionesSchema()
aviones_schema = AvionesSchema(many=True)

@ruta_aviones.route('/aviones', methods=['GET'])
def avion():
    resultall = Avion.query.all() #Select * from Aviones
    resultado_avion= aviones_schema.dump(resultall)
    return jsonify(resultado_avion)

@ruta_aviones.route('/saveavion', methods=['POST'])
def save():
    modelo = request.json['modelo']
    capacidad = request.json['capacidad']
    idaerolinea = request.json['idaerolinea']
    matricula = request.json['matricula']
    new_avion = Avion(modelo,capacidad,idaerolinea,matricula)
    db.session.add(new_avion)
    db.session.commit()    
    return "Datos guardados con éxito"

@ruta_aviones.route('/updateavion', methods=['PUT'])
def Update():
    id = request.json['id']
    modelo = request.json['modelo']
    capacidad = request.json['capacidad']
    idaerolinea = request.json['idaerolinea']
    matricula = request.json['matricula']
    avion = Avion.query.get(id)   
    if avion :
        print(avion)
        avion.modelo = modelo
        avion.capacidad = capacidad
        avion.idaerolinea = idaerolinea
        avion.matricula = matricula
        db.session.commit()
        return "Datos actualizados con éxitos"
    else:
        return "Error"

@ruta_aviones.route('/deleteavion/<id>', methods=['DELETE'])
def eliminar(id):
    avion = Avion.query.get(id)
    db.session.delete(avion)
    db.session.commit()
    return jsonify(avion_schema.dump(avion))