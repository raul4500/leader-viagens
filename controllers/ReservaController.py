from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask import session as cookies_session
from database import*
from repository.__init__ import*
from datetime import*

reserva_controller = Blueprint('reserva_controller', __name__)

reservaRepository = ReservaRepository()
viagemRepository = ViagemRepository()
passageiroRepository = PassageiroRepository()

@reserva_controller.route('/reservar/<int:viagem_id>')
def index(viagem_id):
    passageiro_rgs = request.args.getlist('rg')
    assentos = request.args.getlist('assentos')
    cancelar_reservas = request.args.getlist('cancelar_reserva')
    for c in cancelar_reservas:
        reserva = reservaRepository.getReserva(c)
        if reserva:
            reservaRepository.deleteReserva(c)
    for rg in passageiro_rgs:
        for assento in assentos:
            if reservaRepository.getReserva(assento):
                flash('Assento já reservado.', 'error')
                return redirect(url_for('index_controller.index'))
            if passageiroRepository.getPassageiro(rg):
                passageiro = passageiroRepository.getPassageiro(rg)
            viagem = viagemRepository.getViagem(viagem_id)
            if viagem:
                reservaRepository.createReserva(assento, rg, viagem_id)
                flash('Reserva criada com sucesso!', 'success')
            else:
                flash('Erro ao criar reserva.', 'error')
    return render_template('index.html')
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