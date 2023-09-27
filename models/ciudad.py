from config.db import  db, ma, app

class Ciudad(db.Model):
    __tablename__ = "tblciudad"

    id = db.Column(db.Integer, primary_key =True)
    nombre = db.Column(db.String(50))
    departamento = db.Column(db.String(50))

    def __init__(self, nombre, departamento) :
       self.nombre = nombre
       self.departamento = departamento

with app.app_context():
    db.create_all()

class CiudadesSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre', 'departamento')