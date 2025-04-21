from database import db
from sqlalchemy import*
from sqlalchemy.orm import*
from .Passageiro import Passageiro

# Classe Financeiro
class Financeiro(db.Model):
    __tablename__ = 'financeiro'

    id = db.Column(db.Integer, primary_key=True)
    passageiro_id = db.Column(db.Integer, db.ForeignKey('passageiro.id'), nullable = False)
    valor = db.Column(db.Float)
    data_pagamento = db.Column(db.DateTime)
    data_reserva = db.Column(db.DateTime, nullable = False)
    pagamento_realizado = db.Column(db.Boolean, default = False)

    passageiro = db.relationship("Passageiro", backref="financeiros") #relacionamento passageiro  e financeiro

    def __repr__(self):
        return f"<Financeiro {self.id}>" 

    def toJson(self):
        return {
            "id": self.id,
            "passageiro_id": self.passageiro_id,
            "nome_passageiro": self.passageiro.nome,
            "status_passageiro": self.passageiro.status,
            "valor": self.valor,
            "data_pagamento": self.data_pagamento.strftime('%d-%m-%Y') if self.data_pagamento else None,
            "data_reserva": self.data_reserva.strftime('%d-%m-%Y'),
            "pagamento_realizado": self.pagamento_realizado
        }
