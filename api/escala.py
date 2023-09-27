from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.escala import Escala, EscalasSchema

ruta_escalas = Blueprint("ruta_escala", __name__)

escala_schema = EscalasSchema()
escalas_schema = EscalasSchema(many=True)

@ruta_escalas.route('/escalas', methods=['GET'])
def escala():
    resultall = Escala.query.all() #Select * from Escalas
    resultado_escala= escalas_schema.dump(resultall)
    return jsonify(resultado_escala)

@ruta_escalas.route('/saveescala', methods=['POST'])
def save():
    nombre = request.json['nombre']
    id_vuelo = request.json['id_vuelo']
    aeropuerto = request.json['aeropuerto']
    hora_salida = request.json['hora_salida']
    hora_llegada =request.json['hora_llegad']
    duracion_escala = request.json['duracion_escala']
    new_escala = Escala(nombre, id_vuelo, aeropuerto, hora_salida, hora_llegada, duracion_escala)
    db.session.add(new_escala)
    db.session.commit()    
    return "Datos guardados con éxito"

@ruta_escalas.route('/updateescala', methods=['PUT'])
def Update():
    id = request.json['id']
    nombre = request.json['nombre']
    id_vuelo = request.json['id_vuelo']
    aeropuerto = request.json['aeropuerto']
    hora_salida = request.json['hora_salida']
    hora_llegada =request.json['hora_llegad']
    duracion_escala = request.json['duracion_escala']
    escala = Escala.query.get(id)   
    if escala :
        print(escala) 
        escala.nombre = nombre
        escala.id_vuelo = id_vuelo 
        escala.aeropuerto = aeropuerto 
        escala.hora_salida = hora_salida 
        escala.hora_llegada = hora_llegada
        escala.duracion_escala = duracion_escala 
        db.session.commit()
        return "Datos actualizados con éxitos"
    else:
        return "Error"

@ruta_escalas.route('/deleteescala/<id>', methods=['GET'])
def eliminar(id):
    escala = Escala.query.get(id)
    db.session.delete(escala)
    db.session.commit()
    return jsonify(escala_schema.dump(escala))