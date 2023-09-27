from flask import Flask, jsonify,json
from config.db import  db, ma, app
from api.cliente import Cliente, ruta_clientes
from api.reserva import Reserva, ruta_reservas
from api.cliente import ruta_clientes
from api.ciudad import ruta_ciudades
from api.aeropuerto import ruta_aeropuertos
from api.aerolinea import ruta_aerolineas
from api.aero import ruta_aeros
from api.avion import ruta_aviones
from api.vuelo import ruta_vuelos
from api.escala import ruta_escalas
from api.reserva import ruta_reservas
from api.escala_reserva import ruta_escala_reservas

app.register_blueprint(ruta_clientes,url_prefix = '/api')
app.register_blueprint(ruta_ciudades, url_prefix = '/api')
app.register_blueprint(ruta_aeropuertos, url_prefix = '/api')
app.register_blueprint(ruta_aerolineas, url_prefix = '/api')
app.register_blueprint(ruta_aeros, url_prefix = '/api')
app.register_blueprint(ruta_aviones, url_prefix = '/api')
app.register_blueprint(ruta_vuelos, url_prefix = '/api')
app.register_blueprint(ruta_escalas, url_prefix = '/api')
app.register_blueprint(ruta_reservas, url_prefix = '/api')
app.register_blueprint(ruta_escala_reservas, url_prefix = '/api')

@app.route('/')
def index():
    return "Hola Mundo"

@app.route('/dostablas', methods=['GET'])
def dostabla():
    datos = {}
    resultado = db.session.query(Cliente, Reserva). \
        select_from(Cliente).join(Reserva).all()
    i=0
    for clientes, reservas in resultado:
        i+=1
        datos[i]={
            'cliente':clientes.nombre,
            'reserva': reservas.id
        }
    return datos

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')