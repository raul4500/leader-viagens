from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask import session as cookies_session
from database import*
from repository.__init__ import*
from datetime import*
import re
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import *

passageiro_controller = Blueprint('passageiro_controller', __name__)

passageiroRepository = PassageiroRepository()

def formatar_data(data_americana):
    return datetime.strptime(data_americana, "%Y-%m-%d").strftime("%d-%m-%Y")


def formatar_data_registro(data_hora):
    # Verifica se a entrada é do tipo datetime
    if isinstance(data_hora, datetime):
        # Formatar a data no formato brasileiro (DD/MM/AAAA)
        data_formatada = data_hora.strftime('%d/%m/%Y')
        
        # Formatar a hora no formato (HH:MM:SS)
        hora_formatada = data_hora.strftime('%H:%M:%S')
        
        return [data_formatada, hora_formatada]
    else:
        raise ValueError("O valor fornecido não é do tipo datetime.")
        

def verificarInfo(nome, rg, telefone):
    if nome == "" or rg == "" or telefone == "":
        
        flash('Todos os campos são obrigatórios.', 'error')
        return False

    elif len(nome) < 3 or len(nome.strip().split(' ')) < 2 or nome.endswith(' '):
        flash('Coloque seu nome completo.', 'error')
        return False
    elif len(rg) > 12:
        flash('RG não parece certo.', 'error')
        return False
    elif re.match(r'[a-wA-W]', rg):
        flash('Verique novamente o RG.', 'error')
        return False
    elif len(telefone) != 15:
        flash('Telefone deve ter 11 caracteres.', 'error')
        return False
    elif any(char.isdigit() for char in nome):
        flash('Nome não pode conter números.', 'error')
        return False

    return True

def validar_rg(rg):

    # Remove caracteres não numéricos
    rg = ''.join(filter(str.isdigit, rg))

    # Verifica se o RG possui 9 dígitos
    if len(rg) != 12:
        return False

    # Calcula o dígito verificador
    pesos = [2, 3, 4, 5, 6, 7, 8, 9]
    soma = 0
    for i in range(8):
        soma += int(rg[i]) * pesos[i]

    digito_verificador = soma % 11

    # Verifica se o dígito verificador calculado é igual ao dígito fornecido
    if digito_verificador == 10:
        digito_verificador = 'X'
    elif digito_verificador == 11:
        digito_verificador = 0

    return str(digito_verificador) == rg[8]

@passageiro_controller.route('/passageiros')
def index():
    passageiros = passageiroRepository.getAllPassageiros()
    return render_template('passageiros.html', passageiros=passageiros, formatar_data=formatar_data, formatar_data_registro=formatar_data_registro, str=str)

@passageiro_controller.route('/cadastrar_passageiro/<url>', methods=['GET', 'POST'])
def cadastrar_passageiro(url):
    if request.method == 'POST':
        nome = request.form['nome']
        nascimento = request.form['nascimento']
        if nascimento!='':
            nascimento = formatar_data(nascimento)
        rg = request.form['rg']
        telefone = request.form['telefone']
        status = request.form['status']
        # Convert nascimento to a date object

        # Check if RG already exists
        existing_passageiro = passageiroRepository.getPassageiroByRg(rg)
        if existing_passageiro:
            flash('RG já cadastrado.', 'error')
            return redirect(url_for('passageiro_controller.cadastrar_passageiro'))
        
        if verificarInfo(nome, rg, telefone):
            passageiroRepository.createPassageiro(nome, nascimento, rg, telefone, status)
            flash('passageiro registrado', 'success')
            return redirect(url_for(f'{url}.index'))
    return redirect(url_for(f'{url}.index'))

@passageiro_controller.route('/editar_passageiro/<int:id>', methods=['GET', 'POST'])
def editar_passageiro(id):
    if request.method == 'POST':
        nome = request.form['nome']
        nascimento = request.form['nascimento']
        rg = request.form['rg']
        if nascimento!='':
            nascimento = formatar_data(nascimento)
        telefone = request.form['telefone']
        status = request.form['status']
        if verificarInfo(nome, rg, telefone):  
            passageiroRepository.updatePassageiro(id, nome, nascimento, rg, telefone, status)
            flash('passageiro atualizado', 'success')
            return redirect(url_for('passageiro_controller.index'))
    return redirect(url_for('passageiro_controller.index'))

@passageiro_controller.route('/passageiro/atualizar_status/<int:id>/<status>')
def atualizar_status(id, status):
    passageiroRepository.updateStatus(id, status)
    flash(f'Status de atualizado', 'success')
    return redirect(url_for('index_controller.index'))

@passageiro_controller.route('/deletar_passageiro/<int:id>')
def deletar_passageiro(id):
    passageiroRepository.deletePassageiro(id)
    flash('passageiro deletado', 'success')
    return redirect(url_for('passageiro_controller.index'))


#@passageiros_controller.route('/login', methods=['GET', 'POST'])
#def login():
#    if request.method == 'POST':
#        email = request.form['email']
#        senha = request.form['senha']
#        c = passageiroRepository.getpassageiroByEmail(email)
#        if c:
#            if check_password_hash(c.senha, senha):
#                print('Login efetuado com sucesso')
#                cookies_session['usuario_senha'] = c.senha
#                cookies_session['usuario_email'] = email
#                return redirect(url_for('viagem_controller.index'))
#            else:
#                flash('Senha incorreta')
#                return redirect(url_for('passageiros_controller.login'))
#        else:
#            flash('Email não cadastrado')
#            return redirect(url_for('passageiros_controller.login'))
#    return render_template('login.html')

#@passageiros_controller.route('/logout')
#def logout():
#    cookies_session.pop('usuario_email', None)
#    cookies_session.pop('usuario_senha', None)
#    return redirect(url_for('viagem_controller.index'))