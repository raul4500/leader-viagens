from database import db
from sqlalchemy import*
from sqlalchemy.orm import*


class Pagamento(db.Model):
    __tablename__ = 'pagamento'
    id = db.Column(db.Integer, primary_key=True)
    data_pagamento = db.Column(db.Date, nullable=False)
    valor = db.Column(db.Float, nullable=False)
    forma_pagamento = db.Column(db.String(20), nullable=False)
    destino = db.Column(db.String(200), nullable=False)

    passageiros = relationship("Passageiro", secondary="passageiro_pagamento", back_populates="pagamentos")

    def __repr__(self):
        return f"<Pagamento {self.id} de {self.valor} para Reserva {self.reserva_id}>"

    def toJson(self):
        return {
            "id": self.id,
            "data_pagamento": self.data_pagamento.strftime('%Y-%m-%d %H:%M:%S'),
            "valor": self.valor,
            "forma_pagamento": self.forma_pagamento,
            "destino": self.destino
        }