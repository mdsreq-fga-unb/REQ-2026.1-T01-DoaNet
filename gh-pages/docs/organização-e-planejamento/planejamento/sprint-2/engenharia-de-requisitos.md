# Sprint 2 — Engenharia de Requisitos

[← Voltar ao Objetivo Geral](objetivo-geral.md)

Atividades de Engenharia de Requisitos realizadas na Sprint 2 e suas evidências.

## Verificação de Requisitos (INVEST)

Critérios INVEST aplicados no Sprint Planning para confirmar a prontidão das histórias antes do início do desenvolvimento.

| User Story | I | N | V | E | S | T |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **US17** — Criar publicação no feed | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **US18** — Deletar publicação no feed | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **US19** — Atualizar publicação no feed | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

> **I** — Independente · **N** — Negociável · **V** — Valiosa · **E** — Estimável · **S** — Suficientemente pequena · **T** — Testável

## Critérios de Aceite — Evidências de Cumprimento

Verificação formal dos critérios das histórias na revisão da sprint.

**US17 — Criar publicação no feed**

- ✅ Administrador cria publicação normal com título, texto e imagem opcional
- ✅ Publicação exibida imediatamente no feed após criação
- ✅ Criação restrita a administradores autenticados

**US18 — Deletar publicação no feed**

- ✅ Administrador exclui publicação da sua organização
- ✅ Publicação removida imediatamente do feed após exclusão
- ✅ Exclusão restrita a administradores autenticados

**US19 — Atualizar publicação no feed**

- ✅ Administrador edita título, texto e imagem de publicação existente
- ✅ Alterações refletidas imediatamente no feed após salvar
- ✅ Edição restrita a administradores autenticados

> Critérios de aceite completos de cada US em [User Stories](user-stories.md).

## Organização e Atualização do Backlog

Escopo redefinido após pivoteamento (nova stack: FastAPI + MongoDB + Flutter + Streamlit); refinamento do USM realizado na semana intermediária da sprint.

**Evidências:** [Ata 2 — Planejamento e Pivoteamento (04/05)](../../../atas/ata2_04_05_2026.md) · [Ata de Refinamento S2 (05/05)](../../../atas/ata_refinamento_s2_05_05_2026.md)

## Validação de Requisitos

Feed com CRUD de posts demonstrado ao cliente em 12/05 — aprovação formal do incremento pelo stakeholder.

**Evidências:** [Ata de Validação S2 — 12/05/2026](../../../atas/ata4_12_05_2026.md)
