from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask import session as cookies_session
from database import*
from repository.__init__ import*
from datetime import*

viagem_controller = Blueprint('viagem_controller', __name__)

viagemRepository = ViagemRepository()
clienteRepository = PassageiroRepository()
passageiroRepository = PassageiroRepository()
reservaRepository = ReservaRepository()

def formatar_data(data):
    try:
        date_obj = datetime.strptime(data, "%Y-%m-%d")
        return date_obj.strftime("%d/%m")
    except ValueError:
        return "Data inválida"

@viagem_controller.route('/viagens')
def index():
    viagens = viagemRepository.getAllViagens()
    return render_template('viagens.html', viagens=viagens, formatar_data=formatar_data)

@viagem_controller.route('/cadastrar_viagem', methods=['GET','POST'])
def cadastrar_viagem():
    if request.method == 'POST':
        destino = request.form['destino']
        data_inicio = request.form['data_inicio']
        data_fim = request.form['data_fim']
        preco = request.form['preco']
        qtd_assentos = request.form['qtd_assentos']
        assentos_indisponiveis = None
        tipo_onibus = request.form.get('tipo_onibus')
        descricao = request.form['descricao']
        inclusos = request.form['inclusos']
        viagemRepository.createViagem(destino, data_inicio, data_fim, preco, qtd_assentos, assentos_indisponiveis, tipo_onibus, descricao, inclusos)
        flash('Viagem adicionada com sucesso.', 'success')
        return redirect(url_for('viagem_controller.index'))
    return redirect(url_for('viagem_controller.index'))

@viagem_controller.route('/deletar_viagem/<int:viagem_id>', methods=['GET'])
def delete_viagem(viagem_id):
    viagemRepository.deleteViagem(viagem_id)
    flash('Viagem deletada com sucesso.', 'success')
    return redirect(url_for('viagem_controller.index'))

@viagem_controller.route('/editar_viagem/<int:id>', methods=['GET', 'POST'])
def editar_viagem(id):
    if request.method == 'POST':
        destino = request.form['destino']
        data_inicio = request.form['data_inicio']
        data_fim = request.form['data_fim']
        preco = request.form['preco']
        qtd_assentos = request.form['qtd_assentos']
        tipo_onibus = request.form.get('tipo_onibus')
        descricao = request.form['descricao']
        inclusos = request.form['inclusos']
        try:
            data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d')
        except ValueError:
            flash('Data inválida.', 'error')
            return redirect(url_for('viagem_controller.index'))
        try:
            data_fim = datetime.strptime(data_fim, '%Y-%m-%d')
        except ValueError:
            flash('Data inválida.', 'error')
            return redirect(url_for('viagem_controller.index'))
        viagemRepository.updateViagem(id, destino, data_inicio, data_fim, preco, qtd_assentos, tipo_onibus, descricao, inclusos)
        flash('Viagem editada com sucesso.', 'success')
        return redirect(url_for('viagem_controller.index'))
    return redirect(url_for('viagem_controller.index'))

@viagem_controller.route('/viagem/<int:viagem_id>')
def viagem(viagem_id):
    passageiros = passageiroRepository.getAllPassageiros()
    viagem = viagemRepository.getViagem(viagem_id)
    reservas = reservaRepository.getReservasByViagem(viagem_id)
    if not viagem:
        flash('Viagem não encontrada.', 'error')
        return redirect(url_for('viagem_controller.index'))
    return render_template('mapa-onibus.html', viagem=viagem, passageiros=passageiros, reservas=reservas, dados=dados(reservas, passageiros), mapa=mapa(viagem, reservas, passageiros), formatar_data=formatar_data, type=type)



def dados(reservas, passageiros):
    # Inicia o código HTML
    html = '''
    <div class="tabela-dados" style="display: none;">
        <table>
            <tr>
                <th>NOME</th>
                <th>RG</th>
                <th>DT-NASCTO</th>
                <th>TELEFONE</th>
                <th>PAGAMENTO</th>
                <th>OBSERVAÇÃO</th>
            </tr>
    '''

    # Itera para gerar a tabela com base nas reservas
    for i in range(36):  # Loop de 0 a 35
        # Flag para verificar se houve alguma reserva
        encontrou_reserva = False
        p = None  # Inicializa a variável do passageiro como None
        for r in reservas:
            if r.assento == i:
                # Encontra o passageiro relacionado à reserva
                for passageiro in passageiros:
                    if passageiro.id == r.passageiro_id or passageiro.rg == r.passageiro_id:
                        # Adiciona o passageiro à lista de passageiros reservados
                        p = passageiro
        if p:  # Verifica se o passageiro existe
            encontrou_reserva = True
            # Adiciona a linha de dados para a reserva
            html += f'''
            <tr>
                <td>{p.nome}</td>
                <td>{p.rg}</td>
                <td>{p.nascimento}</td>
                <td>{p.telefone}</td>
                <td>{p.id}</td>
                <td></td>
            </tr>
            '''


        # Caso não tenha encontrado a reserva para esse assento, adiciona uma linha vazia
        if not encontrou_reserva:
            html += f'''
            <tr>
                <td>{i}</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            '''

    # Fecha a tabela e a div
    html += '''
        </table>
    </div>
    '''

    return html

def mapa(viagem, reservas, passageiros):
    class P:
        def __init__(self, nome=''):
            self.nome = nome
    # Início do código HTML
    html = f"""
    <div id="mapa-onibus" class="mapa-onibus" style="display: block;">
    <table>
        <tbody>
            <tr>
                <td colspan="7" style="height: 50px; font-size: 2.5vw;">
                    <center>
                        <h3>{viagem.destino}</h3>
                    </center>
                </td>
                <td colspan="2" style="background-color: rgb(115, 187, 67);">
                    <center>
                        <h2>Saída: {viagem.data_inicio}</h2>
                    </center>
                </td>
            </tr>
            <tr>
                <td colspan="7">
                    <center>
                        <h2>Mapa de viagem</h2>
                    </center>
                </td>
                <td colspan="2" style="background-color: rgb(115, 187, 67);">
                    <center>
                        <h2>Dezembro</h2>
                    </center>
                </td>
            </tr>
            <tr>
                <td colspan="7">
                    <h2 style="text-align: right; color: red;">R$ {viagem.preco}</h2>
                </td>
                <td colspan="2">
                    <p style="font-size: 14px; color: red;">(PARA MEMBROS DO GRUPO)</p>
                </td>
            </tr>
            <tr>
                <td colspan="9">
                    <center>
                        <h2 style="font-size: 16px; color: red;">OU 6X DE R$ {(viagem.preco / 6):,.2f}</h2>
                    </center>
                </td>
            </tr>
    """
    
    # Condição para verificar assentos
    count = 0
    if viagem.qtd_assentos == 49 or viagem.qtd_assentos > 49 and count == 0:
        html += """
            <tr class="piso">
                <td colspan="9">Piso Superior</td>
            </tr>
        """
    
    for i in range(1, viagem.qtd_assentos + 1, 4):
        if i == 49 and count == 0:
            html += """
            <tr class="piso">
                <td colspan="9">Piso Inferior</td>
            </tr>
            """
            count = 1

        html += "<tr>"
        
        if i % 2 != 0:
            if i == viagem.qtd_assentos:
                p = P()  # Inicializa a variável do passageiro como None
                for r in reservas:
                    if r.assento == i:
                # Encontra o passageiro relacionado à reserva
                        for passageiro in passageiros:
                            if passageiro.id == r.passageiro_id or passageiro.rg == r.passageiro_id:
                        # Adiciona o passageiro à lista de passageiros reservados
                                p = passageiro
                html += f"""
                <td class="assento" id="assento_{i}" style="opacity: 0; border: none"></td>
                <td class="assento" id="assento_{i}">{i}</td>
                <td class="nome" draggable=True ondragstart="drag(event)" id="{i}" name="nome_{i}" onclick="highlightSeat('{i}')" ondragover="allowDrop(event)" ondrop="drop(event)">{p.nome}</td>
                <td class="nome" draggable=True ondragstart="drag(event)" id="{i}" name="nome_{i}" style="opacity: 0; border: none">
                </td>
                """
            elif i + 1 == viagem.qtd_assentos:
                p1 = P() 
                p2 = P()
                for r in reservas:
                    if r.assento == i:
                # Encontra o passageiro relacionado à reserva
                        for passageiro in passageiros:
                            if passageiro.id == r.passageiro_id or passageiro.rg == r.passageiro_id:
                        # Adiciona o passageiro à lista de passageiros reservados
                                p1 = passageiro
                for r in reservas:
                    if r.assento == i+1:
                # Encontra o passageiro relacionado à reserva
                        for passageiro in passageiros:
                            if passageiro.id == r.passageiro_id or passageiro.rg == r.passageiro_id:
                        # Adiciona o passageiro à lista de passageiros reservados
                                p2 = passageiro
                html += f"""
                <td class="assento" id="assento_{i}">{i}</td>
                <td class="assento" id="assento_{i+1}">{i+1}</td>
                <td class="nome" draggable=True ondragstart="drag(event)" id="{i}" name="nome_{i}" onclick="highlightSeat('{i}')" ondragover="allowDrop(event)" ondrop="drop(event)">{p1.nome}</td>
                <td class="nome" draggable=True ondragstart="drag(event)" id="{i+1}" name="nome_{i+1}" onclick="highlightSeat('{i + 1}')" ondragover="allowDrop(event)" ondrop="drop(event)">{p2.nome}</td>
                """
            elif i + 2 == viagem.qtd_assentos:
                p1 = P()  # Inicializa a variável do passageiro como None
                p2 = P()
                p3 = P()
                for r in reservas:
                    if r.assento == i:
                # Encontra o passageiro relacionado à reserva
                        for passageiro in passageiros:
                            if passageiro.id == r.passageiro_id or passageiro.rg == r.passageiro_id:
                        # Adiciona o passageiro à lista de passageiros reservados
                                p1 = passageiro
                for r in reservas:
                    if r.assento == i+1:
                # Encontra o passageiro relacionado à reserva
                        for passageiro in passageiros:
                            if passageiro.id == r.passageiro_id or passageiro.rg == r.passageiro_id:
                        # Adiciona o passageiro à lista de passageiros reservados
                                p2 = passageiro
                for r in reservas:
                    if r.assento == i+2:
                # Encontra o passageiro relacionado à reserva
                        for passageiro in passageiros:
                            if passageiro.id == r.passageiro_id or passageiro.rg == r.passageiro_id:
                        # Adiciona o passageiro à lista de passageiros reservados
                                p3 = passageiro
                html += f"""
                <td class="assento" id="assento_{i}">{i}</td>
                <td class="assento" id="assento_{i+1}">{i+1}</td>
                <td class="nome" draggable=True ondragstart="drag(event)" id="{i}" name="nome_{i}" onclick="highlightSeat('{i}')" ondragover="allowDrop(event)" ondrop="drop(event)">{p1.nome}</td>
                <td class="nome" draggable=True ondragstart="drag(event)" id="{i+1}" name="nome_{i+1}" onclick="highlightSeat('{i + 1}')" ondragover="allowDrop(event)" ondrop="drop(event)">{p2.nome}</td>
                <td class="space"></td>
                <td class="assento" id="assento_{i}" style="opacity: 0; border: none"></td>
                <td class="assento" id="assento_{i+2}">{i+2}</td>
                <td class="nome" draggable=True ondragstart="drag(event)" id="{i+2}" name="nome_{i+2}" onclick="highlightSeat('{i + 2}')" ondragover="allowDrop(event)" ondrop="drop(event)">{p3.nome}</td>
                <td class="nome" draggable=True ondragstart="drag(event)" id="{i}" name="nome_{i}" style="opacity: 0; border: none">
                </td>
                """
            else:
                p1 = P()  # Inicializa a variável do passageiro como None
                p2 = P()
                p3 = P()
                p4 = P()
                for r in reservas:
                    if r.assento == i:
                # Encontra o passageiro relacionado à reserva
                        for passageiro in passageiros:
                            if passageiro.id == r.passageiro_id or passageiro.rg == r.passageiro_id:
                        # Adiciona o passageiro à lista de passageiros reservados
                                p1 = passageiro
                for r in reservas:
                    if r.assento == i+1:
                # Encontra o passageiro relacionado à reserva
                        for passageiro in passageiros:
                            if passageiro.id == r.passageiro_id or passageiro.rg == r.passageiro_id:
                        # Adiciona o passageiro à lista de passageiros reservados
                                p2 = passageiro
                for r in reservas:
                    if r.assento == i+2:
                # Encontra o passageiro relacionado à reserva
                        for passageiro in passageiros:
                            if passageiro.id == r.passageiro_id or passageiro.rg == r.passageiro_id:
                        # Adiciona o passageiro à lista de passageiros reservados
                                p3 = passageiro
                for r in reservas:
                    if r.assento == i+3:
                # Encontra o passageiro relacionado à reserva
                        for passageiro in passageiros:
                            if passageiro.id == r.passageiro_id or passageiro.rg == r.passageiro_id:
                        # Adiciona o passageiro à lista de passageiros reservados
                                p4 = passageiro                
                html += f"""
                <td class="assento" id="assento_{i}">{i}</td>
                <td class="assento" id="assento_{i+1}">{i+1}</td>
                <td class="nome" draggable=True ondragstart="drag(event)" id="{i}" name="nome_{i}" onclick="highlightSeat('{i}')" ondragover="allowDrop(event)" ondrop="drop(event)">{p1.nome}</td>
                <td class="nome" draggable=True ondragstart="drag(event)" id="{i+1}" name="nome_{i+1}" onclick="highlightSeat('{i + 1}')" ondragover="allowDrop(event)" ondrop="drop(event)">{p2.nome}</td>
                <td class="space"></td>
                <td class="assento" id="assento_{i+3}">{i+3}</td>
                <td class="assento" id="assento_{i+2}">{i+2}</td>
                <td class="nome" draggable=True ondragstart="drag(event)" id="{i+3}" name="nome_{i+3}" onclick="highlightSeat('{i + 3}')" ondragover="allowDrop(event)" ondrop="drop(event)">{p4.nome}</td>
            <td class="nome" draggable=True ondragstart="drag(event)" id="{i+2}" name="nome_{i+2}" onclick="highlightSeat('{i + 2}')" ondragover="allowDrop(event)" ondrop="drop(event)">{p3.nome}</td>
                """
        
        html += "</tr>"

    html += "</tbody></table></div></div>"

    return html

#@viagem_controller.route('/add_assento/<int:viagem_id>', methods=['GET', 'POST'])
#def add_assento(viagem_id):
#    if request.method == 'POST':
#        assento = request.form['assento']
#        try:
#            assento = int(assento)
#        except ValueError:
#            flash('Assento deve ser um número.')
#            return redirect(url_for('viagem_controller.add_assento', viagem_id=viagem_id))
#
#        viagem = viagemRepository.getViagemById(viagem_id)
#        if viagem:
#            if viagem.assentos_disponiveis is None:
#                viagem.assentos_disponiveis = []
#            viagem.assentos_disponiveis.append(assento)
#            db.session.commit()
#            flash('Assento adicionado com sucesso.')
#        else:
#            flash('Viagem não encontrada.')
#        return redirect(url_for('viagem_controller.index'))
#    return render_template('add_assento.html', viagem_id=viagem_id)
#
#@viagem_controller.route('/add')
#def add():
#    viagemRepository.createViagem('sp', datetime.strptime('2000-05-10', '%Y-%m-%d'), datetime.strptime('2000-01-02', '%Y-%m-%d'), 450, 50, 50, 'https://www.google.com/imgres?q=cataratas%20do%20igua%C3%A7u&imgurl=https%3A%2F%2Fwww.destino.foz.br%2Fwp-content%2Fuploads%2F2022%2F01%2F002-%25E2%2580%2593-Cataratas-do-Iguacu-e1663260066395.jpg&imgrefurl=https%3A%2F%2Fwww.destino.foz.br%2Fatrativo%2Fcataratas-do-iguacu%2F&docid=YIV-_8cJY3u7CM&tbnid=Rop8bFLIsAfZKM&vet=12ahUKEwjRsbGt1a-LAxXzu5UCHTTcCXcQM3oECEEQAA..i&w=1200&h=675&hcb=2&ved=2ahUKEwjRsbGt1a-LAxXzu5UCHTTcCXcQM3oECEEQAA', 'cataratas do iguaçu', 'cataratas')
#    return redirect(url_for('viagem_controller.index'))
#