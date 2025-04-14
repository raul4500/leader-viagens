from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask import session as cookies_session
from database import*
from repository.__init__ import*
from datetime import*

reserva_controller = Blueprint('reserva_controller', __name__)

reservaRepository = ReservaRepository()
viagemRepository = ViagemRepository()
passageiroRepository = PassageiroRepository()

@reserva_controller.route('/reservar/<int:viagem_id>/<passageiro_rg>/<assentos>/<cancelar_reservas>', methods=['GET', 'POST'])
def index(viagem_id, passageiro_rg, assentos, cancelar_reservas):
    print('viagem_id:', viagem_id)
    print('passageiro_rg:', passageiro_rg)
    print('assentos:', assentos)
    print('cancelar_reservas:', cancelar_reservas)
    viagem = viagemRepository.getViagem(viagem_id)
    return
    if passageiro and viagem:
        reservaRepository.createReserva(assento, passageiro_rg, viagem_id)
        flash('Reserva criada com sucesso!', 'success')
        print('Reserva criada com sucesso!')
    else:
        flash('Erro ao criar reserva.', 'error')
        print('Erro ao criar reserva.')
    return redirect(url_for('viagem_controller.viagem', viagem_id=viagem_id))

@reserva_controller.route('/deletar_reserva/<int:reserva_id>', methods=['GET', 'POST'])
def deletar_reserva(reserva_id):
    reserva = reservaRepository.getReserva(reserva_id)
    if reserva:
        reservaRepository.deleteReserva(reserva_id)
        flash('Reserva deletada com sucesso!', 'success')
    else:
        flash('Erro ao deletar reserva.', 'error')
    return redirect(url_for('index_controller.index'))