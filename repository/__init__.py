from .ViagemRepository import *
from .ReservaRepository import *
from .PassageiroRepository import *
from .PagamentoRepository import *
from .LembreteRepository import *
from .FinanceiroRepository import *
from .Pagamento_PassageiroRepository import *

sidebar = """
<aside class="sidebar" aria-label="Menu Lateral">
    <div class="sidebar-group sidebar-group-main">
        <a href="/" data-nav-path="/" title="Visão Geral">
            <div class="sidebar-item"><i class="bi bi-grid-fill"></i></div>
        </a>
        <a href="/passageiros" data-nav-path="/passageiros" title="Passageiros">
            <div class="sidebar-item"><i class="bi bi-people"></i></div>
        </a>
        <a href="/viagens" data-nav-path="/viagens" title="Viagens e Ônibus">
            <div class="sidebar-item"><i class="bi bi-bus-front"></i></div>
        </a>
        <a href="/pagamentos" data-nav-path="/pagamentos" title="Pagamentos">
            <div class="sidebar-item"><i class="bi bi-wallet2"></i></div>
        </a>
    </div>
</aside>
<script>
(function() {
    const path = window.location.pathname;
    document.querySelectorAll('[data-nav-path]').forEach(el => {
        const target = el.getAttribute('data-nav-path');
        const isViagemSub = (target === '/viagens' && path.startsWith('/viagem'));
        if (path === target || isViagemSub) {
            el.classList.add('active');
            el.setAttribute('aria-current', 'page');
            const item = el.querySelector('.sidebar-item');
            if (item) item.classList.add('active');
        }
    });
})();
</script>
"""
