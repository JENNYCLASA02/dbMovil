from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.ciudad import Ciudad, CiudadesSchema

ruta_ciudades = Blueprint("ruta_ciudad", __name__)

ciudad_schema = CiudadesSchema()
ciudades_schema = CiudadesSchema(many=True)

@ruta_ciudades.route('/ciudades', methods=['GET'])
def ciudad():
    resultall = Ciudad.query.all() #Select * from Ciudades
    resultado_ciudad= ciudades_schema.dump(resultall)
    return jsonify(resultado_ciudad)

@ruta_ciudades.route('/saveciudad', methods=['POST'])
def save():
    nombre = request.json['nombre']
    departamento = request.json['departamento']
    new_ciudad = Ciudad(nombre,departamento)
    db.session.add(new_ciudad)
    db.session.commit()    
    return "Datos guardados con éxito"

@ruta_ciudades.route('/updateciudad', methods=['PUT'])
def Update():
    id = request.json['id']
    nombre = request.json['nombre']
    departamento = request.json['departamento']
    ciudad = Ciudad.query.get(id)   
    if ciudad :
        print(ciudad) 
        ciudad.nombre = nombre
        ciudad.departamento = departamento
        db.session.commit()
        return "Datos actualizados con éxitos"
    else:
        return "Error"

@ruta_ciudades.route('/deleteciudad/<id>', methods=['DELETE'])
def eliminar(id):
    ciudad = Ciudad.query.get(id)
    db.session.delete(ciudad)
    db.session.commit()
    return jsonify(ciudad_schema.dump(ciudad))