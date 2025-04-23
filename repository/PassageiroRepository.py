from dao.PassageiroDao import *

class PassageiroRepository:
    def __init__(self):
        self.passageiroDao = PassageiroDao()

    def getAllPassageiros(self):
        return self.passageiroDao.getAllPassageiros()

    def getPassageiro(self, id):
        return self.passageiroDao.getPassageiro(id)
    
    def getPassageiroByRg(self, rg):
        return self.passageiroDao.getPassageiroByRg(rg)

    def createPassageiro(self, nome, nascimento, rg, telefone, status):
        return self.passageiroDao.addPassageiro(nome, nascimento, rg, telefone, status)

    def updatePassageiro(self, id, nome, nascimento, rg, telefone, status):
        return self.passageiroDao.attPassageiro(id, nome, nascimento, rg, telefone, status)
    
    def updateStatus(self, rg, status):
        return self.passageiroDao.attStatus(rg, status)

    def deletePassageiro(self, id):
        return self.passageiroDao.delPassageiro(id)