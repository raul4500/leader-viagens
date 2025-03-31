from dao.__init__ import *

class ReservaRepository:
    def __init__(self):
        self.reservaDao = ReservaDao()

    def getAllReservas(self):
        return self.reservaDao.getAllReservas()

    def getReserva(self, id):
        return self.reservaDao.getReserva(id)

    def createReserva(self, assento, passageiro_id, viagem_id):
        return self.reservaDao.addReserva (assento, passageiro_id, viagem_id)

    def updateReserva(self, id, assento, passageiro_id, viagem_id):
        return self.reservaDao.attReserva(id, assento, passageiro_id, viagem_id)

    def deleteReserva(self, id):
        return self.reservaDao.delReserva(id)