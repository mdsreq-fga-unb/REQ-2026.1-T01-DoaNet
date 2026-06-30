# Sprint 3 — User Stories

[← Voltar ao Objetivo Geral](objetivo-geral.md)

## US17 — Criar publicação no feed (evento)

> Como administrador da organização, quero criar uma nova publicação no feed (normal ou evento), para me comunicar com os apoiadores.

**Critérios de aceite:**

- O administrador consegue criar uma publicação de evento com título, texto, data do evento e imagem opcional.
- A publicação de evento é exibida imediatamente no feed após criação.
- O usuário consegue se inscrever no evento a partir da publicação.
- Apenas administradores autenticados conseguem criar publicações.

**Protótipo da US:** _Captura do protótipo de alta fidelidade desta US a ser inserida._

**Rota de acesso (Streamlit — painel admin):** `http://localhost:8501` → seção **📋 Publicações** → aba **➕ Nova publicação** → tipo **📅 Evento**

---

## US09 — Inscrever-se em evento

> Como usuário, quero me inscrever para atender a um evento divulgado, para confirmar minha presença e participação.

**Critérios de aceite:**

- O usuário consegue se inscrever em um evento a partir da publicação no feed.
- A inscrição é registrada e visível para o administrador.
- O usuário recebe confirmação visual após inscrição bem-sucedida.
- O sistema impede inscrição duplicada no mesmo evento.

**Protótipo da US:** _Captura do protótipo de alta fidelidade desta US a ser inserida._

**Fluxo de navegação (aplicativo mobile):** `Abrir app → aba Feed → publicação de evento → Inscrever-se → Confirmação`

---

## US11 — Autenticar administradores

> Como administrador, quero me autenticar na plataforma, para acessar o painel de gestão correspondente ao meu nível hierárquico.

**Critérios de aceite:**

- O administrador consegue fazer login com credenciais válidas (e-mail + senha).
- Credenciais inválidas retornam mensagem de erro sem expor detalhes técnicos.
- Após autenticação, o painel exibe apenas as funcionalidades do nível hierárquico do admin.
- A sessão é encerrada após logout explícito.

**Protótipo da US:** _Captura do protótipo de alta fidelidade desta US a ser inserida._

**Rota de acesso (Streamlit — painel admin):** `http://localhost:8501` → tela de **Login** do painel administrativo

---

> Evidências de cumprimento dos critérios: [Engenharia de Requisitos — Critérios de Aceite](engenharia-de-requisitos.md#criterios-de-aceite)
