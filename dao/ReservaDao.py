from models.__init__ import*

class ReservaDao:
    @staticmethod
    def getReserva(id):
        return Reserva.query.get(id)

    @staticmethod
    def getAllReservas():
        return Reserva.query.all()
    
    @staticmethod
    def getReservasByViagem(viagem_id):
        return Reserva.query.filter_by(viagem_id=viagem_id).all()
    
    @staticmethod
    def getReservaByAssento(assento_id):
        return Reserva.query.filter_by(assento=assento_id).first()

    @staticmethod
    def addReserva(assento, passageiro_id, viagem_id):
        reserva = Reserva(assento=assento, passageiro_id=passageiro_id, viagem_id=viagem_id)
        db.session.add(reserva)
        db.session.commit()
        return reserva.toJson()

    @staticmethod
    def attReserva(id, assento, passageiro_id, viagem_id):
        reserva = ReservaDao.getReserva(id)
        if reserva:
            reserva.assento = assento
            reserva.passageiro_id = passageiro_id
            reserva.viagem_id = viagem_id
            db.session.commit()
        return reserva.toJson()

    @staticmethod
    def delReserva(id):
        reserva = ReservaDao.getReserva(id)
        if reserva:
            db.session.delete(reserva)
            db.session.commit()
        return reserva.toJson()