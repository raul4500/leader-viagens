from database import db
from sqlalchemy import *
from sqlalchemy.orm import *
from datetime import datetime

# Classe Passageiro
class Passageiro(db.Model):
    __tablename__ = 'passageiro'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    nascimento = db.Column(db.String(10), nullable=True)
    rg = db.Column(db.String(9), nullable=True)
    cpf = db.Column(db.String(11), nullable=True)
    telefone = db.Column(db.String(11), nullable=True)
    status = db.Column(db.String(30), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Novo campo

    pagamentos = relationship("Pagamento", secondary="passageiro_pagamento", back_populates="passageiros")
    # Relacionamento: Um Passageiro pode ter várias reservas

    def __repr__(self):
        return f"<Passageiro {self.nome}>"

    def toJson(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "nascimento": self.nascimento,
            "rg": self.rg,
            "cpf": self.cpf,
            "telefone": self.telefone,
            "status": self.status,
            "created_at": self.created_at,  # Incluindo o novo campo no JSON
            "pagamentos": [pagamento.toJson() for pagamento in self.pagamentos]
        }