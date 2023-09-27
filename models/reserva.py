from config.db import  db, ma, app

class Reserva(db.Model):
    __tablename__ = "tblreserva"

    id = db.Column(db.Integer, primary_key =True)
    idcliente = db.Column(db.Integer, db.ForeignKey('tblcliente.id'))
    fecha_reserva = db.Column(db.DateTime)
    fecha_viaje = db.Column(db.DateTime)
    estado_reserva = db.Column(db.String(50))
    num_asiento = db.Column(db.Integer)
    tipo_asiento = db.Column(db.String(50))
    precio = db.Column(db.Double)
    vuelo = db.Column(db.Integer, db.ForeignKey('tblvuelo.id'))
    metodo_pago = db.Column(db.Double)

    def __init__(self, idcliente, fecha_reserva,fecha_viaje,estado_reserva, num_asiento, tipo_asiento, precio,vuelo, metodo_pago) :
       self.idcliente = idcliente
       self.fecha_reserva = fecha_reserva
       self.fecha_viaje = fecha_viaje
       self.estado_reserva = estado_reserva
       self.num_asiento = num_asiento
       self.tipo_asiento = tipo_asiento
       self.precio = precio
       self.vuelo = vuelo
       self.metodo_pago = metodo_pago


with app.app_context():
    db.create_all()

class ReservasSchema(ma.Schema):
    class Meta:
        fields = ('id','idcliente','fecha reserva','fecha_viaje','estado_reserva','num_asiento','tipo_asiento','precio','vuelo','metodo_pago')
