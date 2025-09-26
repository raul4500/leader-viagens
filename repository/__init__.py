from .ViagemRepository import *
from .ReservaRepository import *
from .PassageiroRepository import *
from .PagamentoRepository import *
from .LembreteRepository import *
from .FinanceiroRepository import *
from .Pagamento_PassageiroRepository import *

sidebar = """
    <div class="main">
        <div class="sidebar">
            <a href="/">
                <div class="sidebar-item"><i class="bi bi-house-fill"></i></div>
            </a>
            <a href="/passageiros">
                <div class="sidebar-item"><i class="bi bi-person-fill"></i></div>
            </a>
            <a href="/viagens">
                <div class="sidebar-item"><i class="bi bi-airplane-fill"></i></div>
            </a>
            <a href="/pagamentos">
                <div class="sidebar-item"><i class="bi bi-credit-card-fill"></i></div>
            </a>
            <a href="" class="bell">
                <div class="sidebar-item"><i class="bi bi-bell-fill"></i></div>
            </a>
    </div>"""