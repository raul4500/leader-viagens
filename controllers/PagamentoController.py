from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask import session as cookies_session
from database import*
from repository.__init__ import*
from datetime import*


pagamento_controller = Blueprint('pagamento_controller', __name__)

pagamentoRepository = PagamentoRepository()

@pagamento_controller.route('/pagamentos')
def index():
    pagamentos = pagamentoRepository.getAllPagamentos()
    ultimos_pagamentos = ({"passageiro": {"nome": "Raul"}, "valor": 200, "data_pagamento": "2025-09-21"})
    return render_template('pagamentos.html', sidebar=sidebar, pagamentos=pagamentos, ultimos_pagamentos=ultimos_pagamentos)

@pagamento_controller.route('/registrar_pagamento/<url>', methods=['GET', 'POST'])
def registrar_pagamento(url):
    if request.method == 'POST':
        valor = request.form['valor']
        data_pagamento = request.form['data_pagamento']
        data_pagamento = datetime.strptime(data_pagamento, '%Y-%m-%d').date()
        forma_pagamento = request.form['forma_pagamento']
        destino = request.form['destino']
        pagamentoRepository.createPagamento(data_pagamento, valor, forma_pagamento, destino)
        flash('Pagamento registrado com sucesso!', 'success')
        return redirect(url_for(f'{url}.index'))
    return render_template('pagamentos.html', url=url, sidebar=sidebar)