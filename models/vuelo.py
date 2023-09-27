from config.db import  db, ma, app

class Vuelo(db.Model):
    __tablename__ = "tblvuelo"

    id = db.Column(db.Integer, primary_key =True)
    nombre = db.Column(db.String(50))
    hora_salida = db.Column(db.DateTime)
    hora_llegada = db.Column(db.DateTime)
    fecha = db.Column(db.DateTime)
    origen = db.Column(db.Integer,db.ForeignKey('tblciudad.id'))
    destino = db.Column(db.Integer,db.ForeignKey('tblciudad.id'))
    avion = db.Column(db.Integer, db.ForeignKey('tblavion.id'))
    aeropuerto = db.Column(db.Integer,db.ForeignKey('tblaeropuerto.id'))


    def __init__(self, nombre, hora_salida, hora_llegada, fecha, origen, destino, avion, aeropuerto) :
       self.nombre = nombre
       self.hora_salida = hora_salida
       self.hora_llegada = hora_llegada
       self.fecha = fecha
       self.origen = origen
       self.destino = destino
       self.avion = avion
       self.aeropuerto = aeropuerto

with app.app_context():
    db.create_all()

class VuelosSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre','hora_salida','hora_llegada','fecha','origen','destino','avion','aeropuerto')