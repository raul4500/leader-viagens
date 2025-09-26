from sqlalchemy import Column, Integer,Table, ForeignKey
from database import db


# Tabela intermediária para o relacionamento muitos-para-muitos
passageiro_pagamento = db.Table(
    'passageiro_pagamento',
    Column('passageiro_id', Integer, ForeignKey('passageiro.id'), primary_key=True),
    Column('pagamento_id', Integer, ForeignKey('pagamento.id'), primary_key=True)
)