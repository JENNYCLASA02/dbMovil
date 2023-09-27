from config.db import  db, ma, app

class Avion(db.Model):
    __tablename__ = "tblavion"

    id = db.Column(db.Integer, primary_key =True)
    modelo = db.Column(db.String(50))
    capacidad = db.Column(db.Integer)
    idaerolinea = db.Column(db.Integer, db.ForeignKey('tblaerolinea.id'))
    matricula = db.Column(db.String(100))


    def __init__(self, modelo, capacidad, idaerolinea, matricula) :
       self.modelo = modelo
       self.capacidad = capacidad
       self.idaerolinea = idaerolinea
       self.matricula = matricula
with app.app_context():
    db.create_all()

class AvionesSchema(ma.Schema):
    class Meta:
        fields = ('id','modelo', 'capacidad', 'idaerolinea','matricula')
