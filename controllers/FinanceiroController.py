from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask import session as cookies_session
from database import*
from repository.__init__ import*
from datetime import*

financeiro_controller = Blueprint("financeiro_controller", __name__)

@financeiro_controller.route('/financeiro')
def financeiro():
    repos = FinanceiroRepository()
    passageiro_id = request.args.get('passageiro_id')

    try: 
        ultimos_pagamentos = repos.getFinancasRecentes(limit=5)

        if passageiro_id:
            registros_financeiros = repos.getFinancasPassageiros(passageiro_id)
            flash(f"Filtrar passageiros por ID: { passageiro_id}", "info")
        else: 
            registros_financeiros = repos.getAllFinancas()
        
        return render_template("financeiro.html", ultimos_pagamentos=ultimos_pagamentos, registros_financeiros=registros_financeiros)

    except Exception as e:
        flash(f"Erro: {str(e)}", "error")
        return render_template("financeiro.html", ultimos_pagamentos = [], registros_financeiros=[])