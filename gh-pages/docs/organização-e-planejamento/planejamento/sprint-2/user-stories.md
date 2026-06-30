# Sprint 2 — User Stories

[← Voltar ao Objetivo Geral](objetivo-geral.md)

## US17 — Criar publicação no feed (post normal)

> Como administrador da organização, quero criar uma nova publicação no feed (normal ou evento), para me comunicar com os apoiadores.

**Critérios de aceite:**

- O administrador consegue criar uma publicação normal com título, texto e imagem opcional.
- O administrador consegue criar uma publicação de evento com título, texto, data do evento e imagem opcional.
- A publicação é exibida imediatamente no feed após criação.
- Apenas administradores autenticados conseguem criar publicações.

**Protótipo da US:** _Captura do protótipo de alta fidelidade desta US a ser inserida._

**Rota de acesso (Streamlit — painel admin):** `http://localhost:8501` → seção **📋 Publicações** → aba **➕ Nova publicação**

---

## US18 — Deletar publicação no feed

> Como administrador da organização, quero deletar uma publicação no feed, para remover um aviso incorreto ou que não seja mais pertinente.

**Critérios de aceite:**

- O administrador consegue excluir qualquer publicação do feed da sua organização.
- A publicação é removida imediatamente do feed após exclusão.
- Apenas administradores autenticados conseguem excluir publicações.

**Protótipo da US:** _Captura do protótipo de alta fidelidade desta US a ser inserida._

**Rota de acesso (Streamlit — painel admin):** `http://localhost:8501` → seção **📋 Publicações** → aba **🗂️ Gerenciar** → **🗑️ Remover**

---

## US19 — Atualizar publicação no feed

> Como administrador da organização, quero atualizar uma publicação no feed, para corrigir ou adicionar detalhes importantes.

**Critérios de aceite:**

- O administrador consegue editar título, texto e imagem de uma publicação existente.
- As alterações são refletidas imediatamente no feed após salvar.
- Apenas administradores autenticados conseguem editar publicações.

**Protótipo da US:** _Captura do protótipo de alta fidelidade desta US a ser inserida._

**Rota de acesso (Streamlit — painel admin):** `http://localhost:8501` → seção **📋 Publicações** → aba **🗂️ Gerenciar** → **💾 Salvar alterações**

---

> Evidências de cumprimento dos critérios: [Engenharia de Requisitos — Critérios de Aceite](engenharia-de-requisitos.md#criterios-de-aceite-evidencias-de-cumprimento)
