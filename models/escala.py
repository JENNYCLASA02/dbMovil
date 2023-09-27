from config.db import  db, ma, app

class Escala(db.Model):
    __tablename__ = "tblescala"

    id = db.Column(db.Integer, primary_key =True)
    nombre = db.Column(db.String(50))
    id_vuelo = db.Column(db.Integer, db.ForeignKey('tblvuelo.id'))
    aeropuerto = db.Column(db.Integer,db.ForeignKey('tblaeropuerto.id'))
    hora_salida = db.Column(db.DateTime)
    hora_llegada = db.Column(db.DateTime)
    duracion_escala = db.Column(db.Time)

    def __init__(self, id_vuelo, nombre, aeropuerto, hora_salida, hora_llegada, duracion_escala) :
       self.id_vuelo = id_vuelo
       self.nombre = nombre
       self.aeropuerto = aeropuerto
       self.hora_salida = hora_salida
       self.hora_llegada = hora_llegada
       self.duracion_escala = duracion_escala

with app.app_context():
    db.create_all()

class EscalasSchema(ma.Schema):
    class Meta:
        fields = ('id','id_vuelo','nombre', 'aeropuerto','hora_salida','hora_llegada','duracion_escala')
