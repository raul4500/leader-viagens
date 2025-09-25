from dao.PagamentoDao import *

class PagamentoRepository:
    def __init__(self):
        self.pagamentoDao = PagamentoDao()

    def getAllPagamentos(self):
        return self.pagamentoDao.getAllPagamentos()

    def getPagamento(self, id):
        return self.pagamentoDao.getPagamento(id)

    def createPagamento(self, data_pagamento, valor, forma_pagamento, destino):
        return self.pagamentoDao.addPagamento(data_pagamento, valor, forma_pagamento, destino)

    def updatePagamento(self, id, data_pagamento, valor, forma_pagamento, destino):
        return self.pagamentoDao.attCliente(id, data_pagamento, valor, forma_pagamento, destino)

    def deletePagamento(self, id):
        return self.pagamentoDao.delPagamento(id)
