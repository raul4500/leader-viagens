from models.Pagamento import *

class PagamentoDao:
    @staticmethod
    def getPagamento(id):
        return Pagamento.query.get(id)

    @staticmethod
    def getAllPagamentos():
        return Pagamento.query.all()

    @staticmethod
    def addPagamento(data_pagamento, valor, forma_pagamento, destino):
        pagamento = Pagamento(data_pagamento=data_pagamento, valor=valor, forma_pagamento=forma_pagamento, destino=destino)
        db.session.add(pagamento)
        db.session.commit()
        return pagamento.toJson()

    @staticmethod
    def attPagamento(id, valor, data_pagamento, forma_pagamento, destino):
        pagamento = PagamentoDao.getPagamento(id)
        if pagamento:
            pagamento.valor = valor
            pagamento.data_pagamento = data_pagamento
            pagamento.forma_pagamento = forma_pagamento
            pagamento.destino = destino
            db.session.commit()
        return pagamento.toJson()

    @staticmethod
    def delPagamento(id):
        pagamento = PagamentoDao.getPagamento(id)
        if pagamento:
            db.session.delete(pagamento)
            db.session.commit()
        return pagamento.toJson()