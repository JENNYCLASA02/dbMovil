from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.reserva import Reserva, ReservasSchema

ruta_reservas = Blueprint("ruta_reserva", __name__)

reserva_schema = ReservasSchema()
reservas_schema = ReservasSchema(many=True)

@ruta_reservas.route('/reservas', methods=['GET'])
def reserva():
    resultall = Reserva.query.all() #Select * from Reservas
    resultado_reserva= reservas_schema.dump(resultall)
    return jsonify(resultado_reserva)

@ruta_reservas.route('/savereserva', methods=['POST'])
def save():
    idcliente = request.json ['idcliente']
    fecha_reserva = request.json ['fecha_reserva']
    fecha_viaje = request.json ['fecha_viaje']
    estado_reserva = request.json ['estado_reserva']
    num_asiento = request.json ['num_asiento']
    tipo_asiento = request.json ['tipo_asiento']
    precio =  request.json ['precio']
    vuelo = request.json ['vuelo']
    metodo_pago =  request.json ['metodo_pago']
    new_reserva = Reserva(idcliente,fecha_reserva,fecha_viaje,estado_reserva,num_asiento,tipo_asiento,precio,vuelo,metodo_pago)
    db.session.add(new_reserva)
    db.session.commit()    
    return "Datos guardados con éxito"

@ruta_reservas.route('/updatereserva', methods=['PUT'])
def Update():
    id = request.json['id']
    idcliente = request.json ['idcliente']
    fecha_reserva = request.json ['fecha_reserva']
    fecha_viaje = request.json ['fecha_viaje']
    estado_reserva = request.json ['estado_reserva']
    num_asiento = request.json ['num_asiento']
    tipo_asiento = request.json ['tipo_asiento']
    precio =  request.json ['precio']
    vuelo = request.json ['vuelo']
    metodo_pago =  request.json ['metodo_pago']
    reserva = Reserva.query.get(id)   
    if reserva :
        print(reserva) 
        reserva.idcliente = idcliente
        reserva. fecha_reserva = fecha_reserva
        reserva.fecha_viaje = fecha_viaje
        reserva.estado_reserva = estado_reserva
        reserva.num_asiento = num_asiento
        reserva.tipo_asiento = tipo_asiento
        reserva.precio = precio
        reserva.vuelo = vuelo
        reserva.metodo_pago = metodo_pago
        db.session.commit()
        return "Datos actualizados con éxitos"
    else:
        return "Error"

@ruta_reservas.route('/deletereserva/<id>', methods=['GET'])
def eliminar(id):
    reserva = Reserva.query.get(id)
    db.session.delete(reserva)
    db.session.commit()
    return jsonify(reserva_schema.dump(reserva))
