from flask import *
from database import init_db
from controllers.__init__ import *
from jinja2 import Environment

app = Flask(__name__)
# Função para controlar o fluxo do loop
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
#app.jinja_env.add_extension(WhileExtension)

app.register_blueprint(viagem_controller)
app.register_blueprint(index_controller)
app.register_blueprint(passageiro_controller)
app.register_blueprint(financeiro_controller)
app.register_blueprint(lembrete_controller)
app.register_blueprint(error_controller)
app.register_blueprint(reserva_controller)
app.secret_key = '1234566789'
if __name__ == "__main__":
    init_db(app)
    app.run(debug=True)