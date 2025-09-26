from dao.Pagamento_PassageiroDao import *

class PagamentoPassageiroRepository:
    def __init__(self):
        self.pagamento_passageiroDao = PagamentoPassageiroDao()

    def associar_passageiro(self, pagamento_id, passageiro_id):
        return self.pagamento_passageiroDao.associar_passageiro(pagamento_id, passageiro_id)

