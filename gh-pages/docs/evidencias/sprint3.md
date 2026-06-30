# Evidências — Sprint 3

---

## User Stories

<a id="us09"></a>
### US09 — Inscrever-se em evento

> Como usuário, quero me inscrever para atender a um evento divulgado, para confirmar minha presença e participação.

**Critérios de Aceite:**

- O usuário consegue se inscrever em um evento a partir da publicação no feed.
- A inscrição é registrada e visível para o administrador.
- O usuário recebe confirmação visual após inscrição bem-sucedida.
- O sistema impede inscrição duplicada no mesmo evento.

#### Protótipo de Alta Fidelidade da US

---

<a id="us11"></a>
### US11 — Autenticar administradores

> Como administrador, quero me autenticar na plataforma, para acessar o painel de gestão correspondente ao meu nível hierárquico.

**Critérios de Aceite:**

- O administrador consegue fazer login com credenciais válidas (e-mail + senha).
- Credenciais inválidas retornam mensagem de erro sem expor detalhes técnicos.
- Após autenticação, o painel exibe apenas as funcionalidades do nível hierárquico do admin.
- A sessão é encerrada após logout explícito.

#### Protótipo de Alta Fidelidade da US

---

---

## Engenharia de Requisitos

### Evidências do Processo de ER

#### Verificação de Requisitos — Critérios INVEST

| User Story | I | N | V | E | S | T |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **US17** — Criar publicação no feed (evento) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **US09** — Inscrever-se em evento divulgado | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **US11** — Autenticar-se como administrador | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

> **I** — Independente · **N** — Negociável · **V** — Valiosa · **E** — Estimável · **S** — Suficientemente pequena · **T** — Testável

#### Validação com o Cliente

- [Ata de Validação S3 — 26/05/2026](../atas/ata5_26_05_2026.md): aprovação do feed completo (posts normais + eventos), inscrição em eventos (US09) e módulo de autenticação admin (US11); protótipo final aprovado como referência para as entregas seguintes.

#### Organização do User Story Map

- [Ata de Validação S2 — 12/05/2026](../atas/ata4_12_05_2026.md): encaminhamentos da Sprint 2 utilizados como insumo para o planejamento desta sprint.
- [Ata de Refinamento S3 — 19/05/2026](../atas/ata_refinamento_s3_19_05_2026.md): refinamento do User Story Map e detalhamento das tarefas da sprint.

---

### Reuniões e Cerimônias Realizadas

#### Sprint Planning

> Reunião de definição do escopo, estimativas e comprometimento do time para a sprint.

📄 _Caso a visualização abaixo não funcione, [acesse a ata diretamente](../atas/ata_planejamento_s3_13_05_2026.md)._

!!! success "Sprint Planning Sprint 3 — 13/05/2026 · Discord"

    --8<-- "atas/ata_planejamento_s3_13_05_2026.md"

#### Refinamento do User Story Map

> Reunião interna realizada na semana intermediária da sprint para revisão e detalhamento das histórias do User Story Map.

📄 _Caso a visualização abaixo não funcione, [acesse a ata diretamente](../atas/ata_refinamento_s3_19_05_2026.md)._

!!! info "Refinamento do User Story Map — 19/05/2026 · Discord"

    --8<-- "atas/ata_refinamento_s3_19_05_2026.md"

#### Validação com o Cliente

> Reunião de apresentação do incremento da sprint ao cliente para coleta de feedback e aprovação formal. Participantes: Letícia Vitória (equipe) e Paulo (stakeholder).

📄 _Caso a visualização abaixo não funcione, [acesse a ata diretamente](../atas/ata5_26_05_2026.md)._

!!! success "Aprovação do Feed Completo, Eventos e Admin — 26/05/2026 · Discord · Letícia e Paulo"

    --8<-- "atas/ata5_26_05_2026.md"

#### Retrospectiva da Equipe

> Percepções individuais dos membros sobre a sprint e aprendizados coletivos.

📄 _Caso a visualização abaixo não funcione, [acesse a ata diretamente](../atas/ata_retrospectiva_s3_26_05_2026.md)._

!!! info "Retrospectiva Sprint 3 — 26/05/2026 · Discord"

    --8<-- "atas/ata_retrospectiva_s3_26_05_2026.md"

---

## Engenharia de Software

### Descrição da Entrega

Nesta sprint, o grupo se propôs a implementar posts de eventos com inscrição, adicionar imagens em todos os tipos de post e iniciar o módulo de admin. O objetivo foi refinar os posts comuns, adicionar os eventos e as opções de administrador.

---

### DoR e DoD

#### Definition of Ready — DoR

> Critérios verificados **antes** do início da sprint para garantir que as histórias estavam prontas para desenvolvimento.

| Critério | Status | Evidência |
| :--- | :---: | :--- |
| O requisito possui informação necessária para ser trabalhado? | ✅ | US09, US11 e US17 (extensão para eventos) detalhadas no Story Map com comportamentos de inscrição e autenticação definidos |
| O requisito cabe em uma Sprint? | ✅ | 3 USs concluídas dentro das 2 semanas; encaminhamentos definidos na Ata 4 |
| Os critérios de aceitação estão definidos? | ✅ | US09, US11 e US17 formalizadas no Story Map |
| O requisito está representado por uma história de usuário? | ✅ | Requisitos representados pelas histórias de usuário: US09, US11 e US17 |
| As definições de arquitetura e contratos de API estão claras? | ✅ | Endpoints de eventos e módulo de autenticação Streamlit definidos com base na arquitetura da Sprint 2 |

#### Definition of Done — DoD

> Critérios verificados **ao final** da sprint para confirmar a qualidade e completude das entregas.

| Critério | Status | Evidência |
| :--- | :---: | :--- |
| Entrega um incremento do produto? | ✅ | Feed completo com eventos e inscrição; início do módulo admin entregues |
| Contempla os critérios de aceite estabelecidos? | ✅ | Cliente validou e aprovou o feed completo e o módulo admin na reunião de 26/05 (Ata 5) |
| O desenvolvimento foi concluído integralmente? | ✅ | CRUD de eventos, inscrição em eventos e autenticação admin funcionando de ponta a ponta |
| Os testes foram executados e aprovados? | ✅ | A cobertura de testes mínima foi alcançada através da pipeline atualizada de testes |
| A funcionalidade foi revisada pela equipe? | ✅ | Revisão realizada nos Pull Requests: #36 |
| A documentação e o feedback relevante foram incorporados? | ✅ | Protótipo final alinhado com equipe e validado pelo cliente; feedback da Ata 5 incorporado |

---

### Demonstração em Imagens

![Feed](../assets/Feed.png)

![Feed2](../assets/Feed2.png)

![Adm](../assets/Adm.png)

![Adm2](../assets/Adm2.png)
