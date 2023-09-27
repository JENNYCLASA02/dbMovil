from config.db import  db, ma, app

class Escala_reserva(db.Model):
    __tablename__ = "tblescala_reserva"

    id = db.Column(db.Integer, primary_key =True)
    idreserva = db.Column(db.Integer, db.ForeignKey('tblreserva.id'))
    idescala = db.Column(db.Integer, db.ForeignKey('tblescala.id'))

    def __init__(self, idreserva, idescala) :
       self.idreserva = idreserva
       self.idescala = idescala

with app.app_context():
    db.create_all()

class Escala_reservasSchema(ma.Schema):
    class Meta:
        fields = ('id','idreserva','idescala')