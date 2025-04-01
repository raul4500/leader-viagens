from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask import session as cookies_session
from database import*
from repository.__init__ import*
from datetime import*

reserva_controller = Blueprint('reserva_controller', __name__)

reservaRepository = ReservaRepository()
viagemRepository = ViagemRepository()
passageiroRepository = PassageiroRepository()

@reserva_controller.route('/reservar/<int:assento>/<int:viagem_id>/<int:passageiro_id>', methods=['GET', 'POST'])
def index(assento, viagem_id, passageiro_id):
    passageiro = passageiroRepository.getPassageiro(passageiro_id)
    viagem = viagemRepository.getViagem(viagem_id)
    if passageiro and viagem:
        reservaRepository.createReserva(assento, passageiro_id, viagem_id)
        flash('Reserva criada com sucesso!', 'success')
    else:
        flash('Erro ao criar reserva.', 'error')
    return redirect(url_for('index_controller.index'))

@reserva_controller.route('/deletar_reserva/<int:reserva_id>', methods=['GET', 'POST'])
def deletar_reserva(reserva_id):
    reserva = reservaRepository.getReserva(reserva_id)
    if reserva:
        reservaRepository.deleteReserva(reserva_id)
        flash('Reserva deletada com sucesso!', 'success')
    else:
        flash('Erro ao deletar reserva.', 'error')
    return redirect(url_for('index_controller.index'))