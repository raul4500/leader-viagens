from dao.FinanceiroDao import*

class FinanceiroRepository:
    def __init__(self):
        self.financeiroDao = FinanceiroDao()

    def getAllFinancas(self):
        return self.financeiroDao.getAllFinancas()
    
    def getFinancas(self, id):
        return self.financeiroDao.getFinancas(id)
    
    def getFinancasPassageiros(self, passageiro_id):
        return self.financeiroDao.getFinancasPassageiros(passageiro_id)
    
    def getFinancasRecentes(self, limit=5):
        return self.financeiroDao.getFinancasRecentes(limit)
    
    def criarFinancas(self, passageiro_id, valor, data_reserva, data_pagamento=None, pagamento_realizado=False):
        return self.financeiroDao.addFinanca(
            passageiro_id=passageiro_id,
            valor=valor,
            data_reserva=data_reserva,
            data_pagamento=data_pagamento,
            pagamento_realizado=pagamento_realizado
        )
    
    def attFinanca(self, id, **kwargs):
        return self.financeiroDao.attFinanceiro(id, **kwargs)
    
    def financaPaga(self, id, data_pagamento=datetime.now()):
        return self.financeiroDao.attFinanceiro(
            id,
            pagamento_realizado=True,
            data_pagamento=data_pagamento
        )
    
    def deletarFinanca(self, id):
        return self.financeiroDao.delFinanceiro(id)