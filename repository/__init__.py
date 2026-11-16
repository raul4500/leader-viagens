from .ViagemRepository import *
from .ReservaRepository import *
from .PassageiroRepository import *
from .PagamentoRepository import *
from .LembreteRepository import *
from .FinanceiroRepository import *
from .Pagamento_PassageiroRepository import *

sidebar = """
<header class="topbar" role="banner">
    <div class="topbar-left">
        <a href="/" class="brand-pill" aria-label="Financeiro Leader - Início">
            <span class="brand-logo-icon"><i class="bi bi-compass-fill"></i></span>
            <span class="brand-name">Leader</span>
        </a>
    </div>

    <nav class="topnav-pill" aria-label="Navegação Principal">
        <a href="/" class="topnav-link" data-nav-path="/">Visão Geral</a>
        <a href="/passageiros" class="topnav-link" data-nav-path="/passageiros">Passageiros</a>
        <a href="/viagens" class="topnav-link" data-nav-path="/viagens">Viagens</a>
        <a href="/pagamentos" class="topnav-link" data-nav-path="/pagamentos">Pagamentos</a>
    </nav>

    <div class="topbar-right">
        <div class="topbar-actions-pill">
            <button type="button" class="topbar-icon-btn" onclick="const s = document.querySelector('input[type=text], input[type=search]'); if(s){s.focus(); s.scrollIntoView({behavior:'smooth', block:'center'});}" title="Buscar na página" aria-label="Buscar na página">
                <i class="bi bi-search"></i>
            </button>
            <a href="/#lembretes-card" class="topbar-icon-btn has-dot" title="Lembretes e Avisos" aria-label="Lembretes e Avisos">
                <i class="bi bi-bell"></i>
            </a>
            <a href="/viagens" class="topbar-icon-btn" title="Mapa de Viagens" aria-label="Mapa de Viagens">
                <i class="bi bi-info-circle"></i>
            </a>
        </div>

        <div class="profile-pill">
            <div class="profile-avatar">FL</div>
            <div class="profile-meta">
                <span class="profile-name">Financeiro Leader</span>
                <span class="profile-role">Gestão &amp; Turismo</span>
            </div>
            <i class="bi bi-chevron-down profile-chevron"></i>
        </div>
    </div>
</header>

<aside class="sidebar" aria-label="Menu Lateral">
    <div class="sidebar-group sidebar-group-top">
        <span class="sidebar-mini-icon active" title="Modo Claro Ativo"><i class="bi bi-sun"></i></span>
        <span class="sidebar-mini-icon" title="Plataforma Verificada"><i class="bi bi-shield-check"></i></span>
    </div>

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
        <a href="/#lembretes-card" class="bell" title="Lembretes">
            <div class="sidebar-item"><i class="bi bi-journal-check"></i></div>
        </a>
    </div>

    <div class="sidebar-group sidebar-group-bottom">
        <a href="/viagens" title="Rotas e Assentos">
            <div class="sidebar-item"><i class="bi bi-question-circle"></i></div>
        </a>
        <a href="/" title="Início">
            <div class="sidebar-item"><i class="bi bi-box-arrow-in-right"></i></div>
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