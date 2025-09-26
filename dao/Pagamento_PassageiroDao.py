from models.Pagamento import *
from models.Passageiro import *
class PagamentoPassageiroDao:
    @staticmethod
    def associar_passageiro(pagamento_id, passageiro_id):
        pagamento = Pagamento.query.get(pagamento_id)
        passageiro = Passageiro.query.get(passageiro_id)

        if not pagamento:
            return {"erro": "Pagamento não encontrado"}, 404
        if not passageiro:
            return {"erro": "Passageiro não encontrado"}, 404

        if passageiro not in pagamento.passageiros:
            pagamento.passageiros.append(passageiro)
            db.session.commit()

        return {"mensagem": "Passageiro associado com sucesso"}, 200