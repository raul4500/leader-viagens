from models.Financeiro import*
from datetime import datetime

class FinanceiroDao:
    @staticmethod
    def getFinanca(id):
        return Financeiro.query.get(id)

    @staticmethod
    def getAllFinancas():
        return Financeiro.query.order_by(Financeiro.data_reserva.desc()).all()


    @staticmethod
    def getFinancasPassageiros(passageiro_id):
        return Financeiro.query.filter_by(passageiro_id=passageiro_id).order_by(Financeiro.data_reserva.desc()).all()


    @staticmethod
    def getFinancasRecentes(limit=5):
        return Financeiro.query.order_by(Financeiro.data_reserva.desc()).limit(limit).all()
    


    @staticmethod
    def addFinanca(passageiro_id, valor, data_reserva, data_pagamento = None, pagamento_realizado=False):
        financa = Financeiro(
            passageiro_id = passageiro_id,
            valor = valor,
            data_reserva = data_reserva,
            data_pagamento = data_pagamento,
            pagamento_realizado = pagamento_realizado
        )
        db.session.add(financa)
        db.session.commit()
        return financa

    @staticmethod
    def attFinanca(id, **kwargs):
        financeiro = FinanceiroDao.getFinanca(id)
        if financeiro:
            for key, value in kwargs.items():
                if hasattr(financeiro. key):
                    setattr(financeiro, key, value)
            db.session.commit()
        return financeiro
    
    @staticmethod
    def financaPaga(id, data_pagamento=datetime.now()):
        return FinanceiroDao.attFinanca(id, pagamento_realizado = True, data_pagamento = data_pagamento)

    @staticmethod
    def deletarFinanca(id):
        financeiro = FinanceiroDao.getFinanca(id)
        if financeiro:
            db.session.delete(financeiro)
            db.session.commit()
        return financeiro