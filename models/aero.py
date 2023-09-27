from config.db import  db, ma, app

class Aero(db.Model):
    __tablename__ = "tblaero"

    id = db.Column(db.Integer, primary_key =True)
    idaeropuerto = db.Column(db.Integer, db.ForeignKey('tblaeropuerto.id'))
    idaerolinea = db.Column(db.Integer, db.ForeignKey('tblaerolinea.id'))

    def __init__(self, idaeropuerto, idaerolinea) :
       self.idaeropuerto = idaeropuerto
       self.idaerolinea = idaerolinea

with app.app_context():
    db.create_all()

class AerosSchema(ma.Schema):
    class Meta:
        fields = ('id','idaeropuerto','idaerolinea')