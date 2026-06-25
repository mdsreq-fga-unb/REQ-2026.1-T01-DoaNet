# Evidências — Sprint 4

---

## User Stories

<a id="us04"></a>
### US04 — Visualizar oportunidades de voluntariado

> Como usuário, quero visualizar oportunidades de voluntariado, para encontrar vagas e formas de ajudar a ONG.

**Critérios de Aceite:**

- A listagem exibe todas as oportunidades de voluntariado ativas.
- Cada oportunidade apresenta título, descrição e requisitos.
- A listagem é acessível sem autenticação.

<a id="us08"></a>

#### Protótipo de Alta Fidelidade da US

---

### US08 — Inscrever-se como voluntário

> Como usuário, quero me inscrever para colaborar como voluntário, para participar ativamente preenchendo meus dados dentro do próprio app.

**Critérios de Aceite:**

- O formulário de inscrição coleta nome, contato e motivação do candidato.
- A inscrição é registrada e visível para o administrador no painel Streamlit.
- O usuário recebe confirmação visual após envio bem-sucedido.

<a id="us20"></a>

#### Protótipo de Alta Fidelidade da US

---

### US20 — Registrar oportunidade de voluntariado

> Como administrador da organização, quero registrar uma oportunidade de voluntariado, para divulgar vagas em aberto para os usuários.

**Critérios de Aceite:**

- O administrador consegue criar uma oportunidade informando título, descrição e requisitos.
- A oportunidade é exibida imediatamente na listagem de voluntariado após criação.
- Apenas administradores autenticados conseguem registrar oportunidades.

#### Protótipo de Alta Fidelidade da US

---

<a id="us21"></a>

#### Protótipo de Alta Fidelidade da US

---

### US21 — Deletar oportunidade de voluntariado

> Como administrador da organização, quero deletar uma oportunidade de voluntariado, para encerrar uma vaga já preenchida.

**Critérios de Aceite:**

- O administrador consegue excluir qualquer oportunidade de voluntariado da sua organização.
- A oportunidade é removida imediatamente da listagem após exclusão.
- Apenas administradores autenticados conseguem excluir oportunidades.

#### Protótipo de Alta Fidelidade da US

---

<a id="us22"></a>
### US22 — Atualizar oportunidade de voluntariado

> Como administrador da organização, quero atualizar uma oportunidade de voluntariado, para alterar requisitos ou o escopo da ajuda necessária.

**Critérios de Aceite:**

- O administrador consegue editar título, descrição e requisitos de uma oportunidade existente.
- As alterações são refletidas imediatamente na listagem após salvar.
- Apenas administradores autenticados conseguem editar oportunidades.

#### Protótipo de Alta Fidelidade da US

---

> **Débito técnico:** o preenchimento do formulário da oportunidade de voluntariado (US08 / US20) não foi inteiramente concluído nesta sprint.

---

## Engenharia de Requisitos

### Evidências do Processo de ER

#### Verificação de Requisitos — Critérios INVEST

| User Story | I | N | V | E | S | T |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **US04** — Visualizar oportunidades de voluntariado | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **US08** — Inscrever-se como voluntário | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **US20** — Registrar oportunidade de voluntariado (admin) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **US21** — Deletar oportunidade de voluntariado (admin) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **US22** — Atualizar oportunidade de voluntariado (admin) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

> **I** — Independente · **N** — Negociável · **V** — Valiosa · **E** — Estimável · **S** — Suficientemente pequena · **T** — Testável

#### Critérios de Aceite — Evidências de Cumprimento

- [US04 — Visualizar oportunidades de voluntariado](#us04): ✅ Todos os critérios verificados
- [US08 — Inscrever-se como voluntário](#us08): ⚠️ Critérios parcialmente atendidos — débito técnico no formulário de inscrição
- [US20 — Registrar oportunidade de voluntariado](#us20): ✅ Todos os critérios verificados
- [US21 — Deletar oportunidade de voluntariado](#us21): ✅ Todos os critérios verificados
- [US22 — Atualizar oportunidade de voluntariado](#us22): ✅ Todos os critérios verificados

#### Validação com o Cliente

- [Ata de Validação S4 — 09/06/2026](../atas/ata6_09_06_2026.md): aprovação do módulo de voluntariado (CRUD) e do painel admin; débito técnico de US08 formalmente registrado.

#### Organização do Backlog

- [Ata de Validação S3 — 26/05/2026](../atas/ata5_26_05_2026.md): encaminhamentos da Sprint 3 utilizados como insumo para o planejamento desta sprint.
- [Ata de Validação S4 — 09/06/2026](../atas/ata6_09_06_2026.md): débito técnico de US08 formalizado e encaminhado para a Sprint 5.

---

### Reuniões e Cerimônias Realizadas

#### Sprint Planning

> Reunião de definição do escopo, estimativas e comprometimento do time para a sprint.

📄 _Caso a visualização abaixo não funcione, [acesse a ata diretamente](../atas/ata_planejamento_s4_27_05_2026.md)._

!!! success "Sprint Planning Sprint 4 — 27/05/2026 · Discord"

    --8<-- "atas/ata_planejamento_s4_27_05_2026.md"

#### Refinamento do User Story Map

> Reunião interna realizada na semana intermediária da sprint para revisão e detalhamento das histórias do User Story Map.

📄 _Caso a visualização abaixo não funcione, [acesse a ata diretamente](../atas/ata_refinamento_s4_02_06_2026.md)._

!!! info "Refinamento do User Story Map — 02/06/2026 · Discord"

    --8<-- "atas/ata_refinamento_s4_02_06_2026.md"

#### Validação com o Cliente

> Reunião de apresentação do incremento da sprint ao cliente para coleta de feedback e aprovação formal. Participantes: Letícia Vitória (equipe) e Paulo (stakeholder).

📄 _Caso a visualização abaixo não funcione, [acesse a ata diretamente](../atas/ata6_09_06_2026.md)._

!!! success "Aprovação do Voluntariado e Painel Admin — 09/06/2026 · Discord · Letícia e Paulo"

    --8<-- "atas/ata6_09_06_2026.md"

#### Retrospectiva da Equipe

> Percepções individuais dos membros sobre a sprint e aprendizados coletivos.

📄 _Caso a visualização abaixo não funcione, [acesse a ata diretamente](../atas/ata_retrospectiva_s4_09_06_2026.md)._

!!! info "Retrospectiva Sprint 4 — 09/06/2026 · Discord"

    --8<-- "atas/ata_retrospectiva_s4_09_06_2026.md"

---

## Engenharia de Software

### Descrição da Entrega

Nesta sprint, o grupo se propôs a realizar a parte de colaboração com a organização, registrando a participação em voluntariados e administração do que foi entregue.

**Obs:** Na parte do voluntariado teve um débito técnico onde não foi completado totalmente o preenchimento de formulário da oportunidade de voluntariado.

---

### DoR e DoD

#### Definition of Ready — DoR

> Critérios verificados **antes** do início da sprint para garantir que as histórias estavam prontas para desenvolvimento.

| Critério | Status | Evidência |
| :--- | :---: | :--- |
| O requisito possui informação necessária para ser trabalhado? | ✅ | US04, US08, US20, US21 e US22 detalhadas no Story Map com fluxos de CRUD e inscrição definidos |
| O requisito cabe em uma Sprint? | ✅ | 5 USs do módulo de voluntariado planejadas para 2 semanas; encaminhamentos definidos na Ata 5 |
| Os critérios de aceitação estão definidos? | ✅ | US04, US08, US20, US21 e US22 formalizadas no Story Map |
| O requisito está representado por uma história de usuário? | ✅ | Requisitos representados pelas histórias de usuário: US04, US08, US20, US21 e US22 |
| As definições de arquitetura e contratos de API estão claras? | ✅ | Endpoints de voluntariado e painel admin definidos com base na arquitetura consolidada nas sprints anteriores |

#### Definition of Done — DoD

> Critérios verificados **ao final** da sprint para confirmar a qualidade e completude das entregas.

| Critério | Status | Evidência |
| :--- | :---: | :--- |
| Entrega um incremento do produto? | ✅ | Módulo de voluntariado (CRUD e inscrição) e painel admin entregues e funcionais |
| Contempla os critérios de aceite estabelecidos? | ⚠️ | Cliente aprovou as entregas na Ata 6; débito técnico identificado no formulário de inscrição de voluntariado |
| O desenvolvimento foi concluído integralmente? | ⚠️ | Fluxo de voluntariado funcional, porém formulário de inscrição incompleto (débito técnico registrado na Ata 6) |
| Os testes foram executados e aprovados? | ⚠️ | Ausência da cobertura completa de testes principalmente nas novas alterações feitas no módulo de administrador |
| A funcionalidade foi revisada pela equipe? | ✅ | Revisão realizada nos Pull Requests: #37, #38 |
| A documentação e o feedback relevante foram incorporados? | ✅ | Débito técnico documentado; encaminhamentos para Sprint 5 definidos na Ata 6 |

---

### Demonstração em Imagens

![Colab](../assets/Colab.png)

![Colab2](../assets/Colab2.png)

![Post](../assets/Post.png)

![Gerencia](../assets/Gerencia.png)

![Voluntario](../assets/Voluntario.png)

![Voluntario2](../assets/Voluntario2.png)
