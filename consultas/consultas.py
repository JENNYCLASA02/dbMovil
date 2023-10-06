from config.db import  db, ma, app
from api.cliente import Cliente, ruta_clientes
from api.reserva import Reserva, ruta_reservas
from api.vuelo import Vuelo, ruta_vuelos
from api.ciudad import Ciudad, ruta_ciudades
from api.aeropuerto import Aeropuerto, ruta_aeropuertos
from api.aerolinea import Aerolinea, ruta_aerolineas
from api.avion import Avion, ruta_aviones
from api.escala import Escala, ruta_escalas
from api.escala_reserva import Escala_reserva, ruta_escala_reservas
from api.aero import Aero, ruta_aeros

app.register_blueprint(ruta_reservas, url_prefix = '/api')
app.register_blueprint(ruta_clientes,url_prefix = '/api')
app.register_blueprint(ruta_aeros,url_prefix = '/api')
app.register_blueprint(ruta_vuelos,url_prefix = '/api')
app.register_blueprint(ruta_ciudades,url_prefix = '/api')
app.register_blueprint(ruta_aeropuertos,url_prefix = '/api')
app.register_blueprint(ruta_aerolineas,url_prefix = '/api')
app.register_blueprint(ruta_aviones,url_prefix = '/api')
app.register_blueprint(ruta_escalas,url_prefix = '/api')
app.register_blueprint(ruta_escala_reservas,url_prefix = '/api')


# CONSULTA 01
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

# CONSULTA 02
@app.route('/consultaaereo', methods=['GET'])
def consultaaereo():
    datos = {}
    resultado = db.session.query(Aeropuerto, Ciudad). \
        select_from(Ciudad).join(Aeropuerto).all()
    i=0
    for ciudades, aeropuertos in resultado:
        i+=1
        datos[i]={
            'ciudad':ciudades.nombre,
            'departamento':ciudades.departamento,
            'aerepuerto': aeropuertos.nombre,
            'aerepuerto': aeropuertos.dirección
        }
    return datos

#Consulta 03

@app.route('/consultaraereolinea', methods=['GET'])
def consultaraereolinea():
    datos = {}
    resultado = db.session.query(Aero, Aeropuerto, Aerolinea). \
        select_from(Aeropuerto).join(Aerolinea).join(Aero).all()
    i=0
    for aeropuertos, aerolineas, aeros in resultado:
        i+=1
        datos[i]={
            'nombre_aeropuerto':aeropuertos.nombre,
            'direccion_aeropuerto': aeropuertos.direccion,
            'aerolinea': aerolineas.nombre
        }
    return datos