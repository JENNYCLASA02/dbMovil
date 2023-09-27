from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.escala_reserva import Escala_reserva, Escala_reservasSchema

ruta_escala_reservas = Blueprint("ruta_escala_reserva", __name__)

escala_reserva_schema = Escala_reservasSchema()
escala_reservas_schema = Escala_reservasSchema(many=True)

@ruta_escala_reservas.route('/escala_reservas', methods=['GET'])
def escala_reserva():
    resultall = Escala_reserva.query.all() #Select * from Escala_reservas
    resultado_escala_reserva= escala_reservas_schema.dump(resultall)
    return jsonify(resultado_escala_reserva)

@ruta_escala_reservas.route('/saveescala_reserva', methods=['POST'])
def save():
    idreserva = request.json['idreserva']
    idescala = request.json['idescala']
    new_escala_reserva = Escala_reserva(idreserva,idescala)
    db.session.add(new_escala_reserva)
    db.session.commit()    
    return "Datos guardados con éxito"

@ruta_escala_reservas.route('/updateescala_reserva', methods=['PUT'])
def Update():
    id = request.json['id']
    idreserva = request.json['idreserva']
    idescala = request.json['idescala']
    escala_reserva = Escala_reserva.query.get(id)   
    if escala_reserva :
        print(escala_reserva) 
        escala_reserva.idreserva = idreserva
        escala_reserva.idescala = idescala
        db.session.commit()
        return "Datos actualizados con éxitos"
    else:
        return "Error"

@ruta_escala_reservas.route('/deleteescala_reserva/<id>', methods=['DELETE'])
def eliminar(id):
    escala_reserva = Escala_reserva.query.get(id)
    db.session.delete(escala_reserva)
    db.session.commit()
    return jsonify(escala_reserva_schema.dump(escala_reserva))