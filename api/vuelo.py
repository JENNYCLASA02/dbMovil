from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.vuelo import Vuelo, VuelosSchema

ruta_vuelos = Blueprint("ruta_vuelo", __name__)

vuelo_schema = VuelosSchema()
vuelos_schema = VuelosSchema(many=True)

@ruta_vuelos.route('/vuelos', methods=['GET'])
def vuelo():
    resultall = Vuelo.query.all() #Select * from Vuelos
    resultado_vuelo= vuelos_schema.dump(resultall)
    return jsonify(resultado_vuelo)

@ruta_vuelos.route('/savevuelo', methods=['POST'])
def save():
    nombre = request.json['nombre']
    hora_salida = request.json['hora_salida']
    hora_llegada = request.json['hora_llegada']
    fecha = request.json['fecha']
    origen = request.json['origen']
    destino = request.json['destino']
    avion = request.json['avion']
    aeropuerto = request.json['aeropuerto']
    new_vuelo = Vuelo(nombre, hora_salida, hora_llegada, fecha, origen, destino, avion, aeropuerto)
    db.session.add(new_vuelo)
    db.session.commit()    
    return "Datos guardados con éxito"

@ruta_vuelos.route('/updatevuelo', methods=['PUT'])
def Update():
    id = request.json['id']
    nombre = request.json['nombre']
    hora_salida = request.json['hora_salida']
    hora_llegada = request.json['hora_llegada']
    fecha = request.json['fecha']
    origen = request.json['origen']
    destino = request.json['destino']
    avion = request.json['avion']
    aeropuerto = request.json['aeropuerto']

    vuelo = Vuelo.query.get(id)   
    if vuelo :
        print(vuelo) 
        vuelo.nombre = nombre
        vuelo.hora_salida = hora_salida
        vuelo.hora_llegada = hora_llegada
        vuelo.fecha = fecha
        vuelo.origen = origen
        vuelo.destino = destino
        vuelo.avion = avion
        vuelo.aeropuerto = aeropuerto
        db.session.commit()
        return "Datos actualizados con éxitos"
    else:
        return "Error"

@ruta_vuelos.route('/deletevuelo/<id>', methods=['GET'])
def eliminar(id):
    vuelo = Vuelo.query.get(id)
    db.session.delete(vuelo)
    db.session.commit()
    return jsonify(vuelo_schema.dump(vuelo))