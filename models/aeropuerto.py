from config.db import  db, ma, app

class Aeropuerto(db.Model):
    __tablename__ = "tblaeropuerto"

    id = db.Column(db.Integer, primary_key =True)
    nombre = db.Column(db.String(50))
    idciudad = db.Column(db.Integer, db.ForeignKey('tblciudad.id'))
    direccion = db.Column(db.String(100))


    def __init__(self, nombre, idciudad, direccion) :
       self.nombre = nombre
       self.idciudad = idciudad
       self.direccion = direccion

with app.app_context():
    db.create_all()

class AeropuertosSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre', 'idciudad','direccion')
