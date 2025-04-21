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
    passageiro_rgs = request.args.get('rg').split(',')
    assentos = request.args.get('assentos').split(',')
    cancelar_reservas = request.args.get('cancelar_reserva').split(',')
    for c in cancelar_reservas:
        reserva = reservaRepository.getReservaByAssento(c)
        if reserva:
            reservaRepository.deleteReserva(c)
            flash('Reserva cancelada com sucesso!', 'success')
    for i in range (len(passageiro_rgs)):
        if passageiro_rgs[i] != '':
            passageiro = passageiroRepository.getPassageiroByRg(passageiro_rgs[i])          
            viagem = viagemRepository.getViagem(viagem_id)
            if passageiro and viagem:
                reservaRepository.createReserva(assentos[i], passageiro.id, viagem_id)
                flash('Reserva criada com sucesso!', 'success')
            else:
                flash('Erro ao criar reserva.', 'error')
    return redirect(url_for('viagem_controller.viagem', viagem_id=viagem_id))
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