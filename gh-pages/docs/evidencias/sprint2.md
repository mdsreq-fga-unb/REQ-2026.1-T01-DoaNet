# Evidências — Sprint 2

---

## User Stories

<a id="us02"></a>
### US02 — Visualizar publicações no feed

> Como usuário, quero visualizar as publicações no feed, para me manter atualizado sobre as ações e eventos da organização.

**Critérios de Aceite:**

- O feed exibe publicações em ordem cronológica decrescente.
- Cada publicação apresenta título, data de criação e imagem (quando disponível).
- O feed exibe tanto posts normais quanto posts de eventos.
- O feed é acessível sem autenticação.

#### Protótipo de Alta Fidelidade da US

---

<a id="us17"></a>
### US17 — Criar publicação no feed

> Como administrador da organização, quero criar uma nova publicação no feed (normal ou evento), para me comunicar com os apoiadores.

**Critérios de Aceite:**

- O administrador consegue criar uma publicação normal com título, texto e imagem opcional.
- O administrador consegue criar uma publicação de evento com título, texto, data do evento e imagem opcional.
- A publicação é exibida imediatamente no feed após criação.
- Apenas administradores autenticados conseguem criar publicações.

#### Protótipo de Alta Fidelidade da US

---

<a id="us18"></a>
### US18 — Deletar publicação no feed

> Como administrador da organização, quero deletar uma publicação no feed, para remover um aviso incorreto ou que não seja mais pertinente.

**Critérios de Aceite:**

- O administrador consegue excluir qualquer publicação do feed da sua organização.
- A publicação é removida imediatamente do feed após exclusão.
- Apenas administradores autenticados conseguem excluir publicações.

#### Protótipo de Alta Fidelidade da US

---

<a id="us19"></a>
### US19 — Atualizar publicação no feed

> Como administrador da organização, quero atualizar uma publicação no feed, para corrigir ou adicionar detalhes importantes.

**Critérios de Aceite:**

- O administrador consegue editar título, texto e imagem de uma publicação existente.
- As alterações são refletidas imediatamente no feed após salvar.
- Apenas administradores autenticados conseguem editar publicações.

#### Protótipo de Alta Fidelidade da US

---

---

## Engenharia de Requisitos

### Evidências do Processo de ER

> Atividades de Engenharia de Requisitos realizadas nesta sprint, conforme o processo ScrumXP definido em [Engenharia de Requisitos](../visao_produto/5-EngenhariadeRequisitos.md).

#### Verificação de Requisitos — Critérios INVEST

Aplicado no Sprint Planning para confirmar que as histórias estavam prontas para desenvolvimento antes de entrar na sprint.

| User Story | I | N | V | E | S | T |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **US17** — Criar publicação no feed | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **US18** — Deletar publicação no feed | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **US19** — Atualizar publicação no feed | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

> **I** — Independente · **N** — Negociável · **V** — Valiosa · **E** — Estimável · **S** — Suficientemente pequena · **T** — Testável

#### Critérios de Aceite — Evidências de Cumprimento

Critérios verificados na revisão da sprint e validados com o cliente na [Ata 4](../atas/ata4_12_05_2026.md). Definição completa em [US17 - Criar publicação no feed](#us17), [US18 - Deletar publicação no feed](#us18), [US19 - Atualizar publicação no feed](#us19).

**[US17 - Criar publicação no feed](#us17)**

- ✅ Administrador cria publicação normal com título, texto e imagem opcional
- ✅ Publicação exibida imediatamente no feed após criação
- ✅ Criação restrita a administradores autenticados

**[US18 - Deletar publicação no feed](#us18)**

- ✅ Administrador exclui publicação da sua organização
- ✅ Publicação removida imediatamente do feed após exclusão
- ✅ Exclusão restrita a administradores autenticados

**[US19 - Atualizar publicação no feed](#us19)**

- ✅ Administrador edita título, texto e imagem de publicação existente
- ✅ Alterações refletidas imediatamente no feed após salvar
- ✅ Edição restrita a administradores autenticados

#### Validação de Requisitos — Protótipos e Feedback do Cliente

- Incremento do feed com CRUD de posts demonstrado à cliente (Letícia) e a Paulo na reunião de 12/05.
- Protótipo de baixa/média fidelidade da tela de Feed (Sprint 1) utilizado como referência visual para validação do layout e fluxo.
- Protótipo de baixa/média fidelidade da tela de Colaboração/Voluntariado apresentado e validado pelo cliente na mesma reunião — ver [Ata de Validação S2](../atas/ata4_12_05_2026.md).
- Aprovação formal documentada na [Ata de Validação S2](../atas/ata4_12_05_2026.md) — funcionalidades de criar, editar e deletar posts e protótipo da tela de voluntariado aprovados sem ressalvas.

#### Organização e Atualização — Refinamento do User Story Map

- Backlog revisado e tarefas da sprint detalhadas na reunião interna de 11/05 — ver [Ata 3](../atas/ata3_11_05_2026.md).
- Escopo redefinido após pivoteamento registrado na [Ata 2](../atas/ata2_04_05_2026.md): nova stack (FastAPI + MongoDB + Flutter + Streamlit) e replanejamento completo das histórias de usuário.

---

### Reuniões e Cerimônias Realizadas

#### Sprint Planning

> Reunião de definição do escopo, estimativas e comprometimento do time para a sprint.

📄 _Caso a visualização abaixo não funcione, [acesse a ata diretamente](../atas/ata2_04_05_2026.md)._

!!! success "Alinhamento Estratégico e Pivoteamento — 04/05/2026 · Presencial"

    --8<-- "atas/ata2_04_05_2026.md"

#### Refinamento do User Story Map

> Reunião interna realizada na semana intermediária da sprint para revisão e detalhamento das histórias do User Story Map.

📄 _Caso a visualização abaixo não funcione, [acesse a ata diretamente](../atas/ata_refinamento_s2_05_05_2026.md)._

!!! info "Refinamento do User Story Map pós-pivoteamento — 05/05/2026 · Discord"

    --8<-- "atas/ata_refinamento_s2_05_05_2026.md"

#### Validação com o Cliente

> Reunião de apresentação do incremento da sprint ao cliente para coleta de feedback e aprovação formal. Participantes: Letícia Vitória (equipe) e Paulo (stakeholder).

📄 _Caso a visualização abaixo não funcione, [acesse a ata diretamente](../atas/ata4_12_05_2026.md)._

!!! success "Aprovação do Feed — 12/05/2026 · Discord · Letícia e Paulo"

    --8<-- "atas/ata4_12_05_2026.md"

#### Retrospectiva da Equipe

> Percepções individuais dos membros sobre a sprint e aprendizados coletivos.

📄 _Caso a visualização abaixo não funcione, [acesse a ata diretamente](../atas/ata_retrospectiva_s2_12_05_2026.md)._

!!! info "Retrospectiva Sprint 2 — 12/05/2026 · Discord"

    --8<-- "atas/ata_retrospectiva_s2_12_05_2026.md"

---

## Engenharia de Software

### Descrição da Entrega

Nesta sprint, o grupo se propôs a implementar as funcionalidades centrais da plataforma DoaNet, com foco na criação, edição e deleção de postagens normais (sem nenhum evento atrelado).

---

### DoR e DoD

#### Definition of Ready — DoR

> Critérios verificados **antes** do início da sprint para garantir que as histórias estavam prontas para desenvolvimento.

| Critério | Status | Evidência |
| :--- | :---: | :--- |
| O requisito possui informação necessária para ser trabalhado? | ✅ | US17, US18 e US19 detalhadas no Story Map com personas, objetivos e atividades |
| O requisito cabe em uma Sprint? | ✅ | 3 USs de CRUD de posts normais concluídas dentro das 2 semanas da sprint |
| Os critérios de aceitação estão definidos? | ✅ | US17, US18 e US19 formalizadas no Story Map |
| O requisito está representado por uma história de usuário? | ✅ | Requisitos representados pelas histórias de usuário: US17, US18 e US19 |
| As definições de arquitetura e contratos de API estão claras? | ✅ | Stack redefinida pós-pivoteamento (FastAPI + MongoDB + Flutter + Streamlit) documentada na Ata 2 |

#### Definition of Done — DoD

> Critérios verificados **ao final** da sprint para confirmar a qualidade e completude das entregas.

| Critério | Status | Evidência |
| :--- | :---: | :--- |
| Entrega um incremento do produto? | ✅ | Feed com CRUD de posts normais funcionando ao final da sprint |
| Contempla os critérios de aceite estabelecidos? | ✅ | Cliente validou e aprovou o CRUD do feed na reunião de 12/05 (Ata 4) |
| O desenvolvimento foi concluído integralmente? | ✅ | Criação, edição e deleção de postagens normais funcionando de ponta a ponta |
| Os testes foram executados e aprovados? | ✅ | A cobertura de testes mínima foi alcançada através da pipeline atualizada de testes |
| A funcionalidade foi revisada pela equipe? | ✅ | Revisão realizada nos Pull Requests: #26 |
| A documentação e o feedback relevante foram incorporados? | ✅ | Ajustes do pivoteamento refletidos na implementação conforme Ata 2 e validação da Ata 4 |

---

### Demonstração em Imagens

![Feed](../assets/Feed.png)

![Feed2](../assets/Feed2.png)
