# Evidências — Sprint 2

## User Stories Relacionadas

| US | Descrição |
| :--- | :--- |
| **US17** | Como administrador da organização, quero criar uma nova publicação no feed (normal), para me comunicar com os apoiadores. |
| **US18** | Como administrador da organização, quero deletar uma publicação no feed, para remover um aviso incorreto ou que não seja mais pertinente. |
| **US19** | Como administrador da organização, quero atualizar uma publicação no feed, para corrigir ou adicionar detalhes importantes. |

---

## Descrição da Entrega

Nesta sprint, o grupo se propôs a implementar as funcionalidades centrais da plataforma DoaNet, com foco na criação, edição e deleção de postagens normais (sem nenhum evento atrelado).

---

## DoR e DoD

### Definition of Ready — DoR

> Critérios verificados **antes** do início da sprint para garantir que as histórias estavam prontas para desenvolvimento.

| Critério | Status | Evidência |
| :--- | :---: | :--- |
| O requisito possui informação necessária para ser trabalhado? | ✅ | US17, US18 e US19 detalhadas no Story Map com personas, objetivos e atividades |
| O requisito cabe em uma Sprint? | ✅ | 3 USs de CRUD de posts normais concluídas dentro das 2 semanas da sprint |
| O requisito está representado por uma história de usuário? | ✅ | US17, US18 e US19 formalizadas no Story Map |
| O requisito está mapeado para uma interface (quando necessário)? | ✅ | Interface do feed definida no protótipo de baixa fidelidade validado na Sprint 1 |
| As definições de arquitetura e contratos de API estão claras? | ✅ | Stack redefinida pós-pivoteamento (FastAPI + MongoDB + Flutter + Streamlit) documentada na Ata 2 |

### Definition of Done — DoD

> Critérios verificados **ao final** da sprint para confirmar a qualidade e completude das entregas.

| Critério | Status | Evidência |
| :--- | :---: | :--- |
| Entrega um incremento do produto? | ✅ | Feed com CRUD de posts normais funcionando ao final da sprint |
| Contempla os critérios de aceite estabelecidos? | ✅ | Cliente validou e aprovou o CRUD do feed na reunião de 12/05 (Ata 4) |
| Está documentado para uso? | _a preencher_ | _Descrever atualização do Swagger/OpenAPI e comentários relevantes no código_ |
| Está aderente aos padrões de codificação? | ✅ | Desenvolvido em FastAPI (back-end) e Flutter (front-end) conforme stack definida |
| Mantém os índices de performance do produto? | _a preencher_ | _Descrever métricas ou testes de performance realizados_ |
| O desenvolvimento foi concluído integralmente? | ✅ | Criação, edição e deleção de postagens normais funcionando de ponta a ponta |
| O isolamento de dados e segurança foram validados? | _a preencher_ | _Descrever validação da partition key e isolamento multi-tenant_ |
| A conformidade legal e imutabilidade financeira foram aplicadas? | N/A | Não se aplica — sprint sem funcionalidades de pagamento ou doação |
| Os testes foram executados e aprovados? | _a preencher_ | _Descrever testes unitários e de integração realizados_ |
| A funcionalidade foi revisada pela equipe? | _a preencher_ | _Registrar número ou link do Pull Request no GitHub_ |
| A documentação e o feedback relevante foram incorporados? | ✅ | Ajustes do pivoteamento refletidos na implementação conforme Ata 2 e validação da Ata 4 |

---

## Evidências do Processo de ER

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

Critérios verificados na revisão da sprint e validados com o cliente na [Ata 4](../atas/ata4_12_05_2026.md). Definição completa em [10.3 Critérios de Aceite](../visao_produto/10-story_map.md).

**US17 — Criar publicação no feed (post normal)**

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

#### Validação de Requisitos — Protótipos e Feedback do Cliente

- Incremento do feed com CRUD de posts demonstrado à cliente (Letícia) e a Paulo na reunião de 12/05.
- Protótipo de baixa fidelidade (Sprint 1) utilizado como referência visual para validação do layout e fluxo do feed.
- Aprovação formal documentada na [Ata de Validação S2](../atas/ata4_12_05_2026.md) — funcionalidades de criar, editar e deletar posts aprovadas sem ressalvas.

#### Organização e Atualização — Refinamento do User Story Map

- Backlog revisado e tarefas da sprint detalhadas na reunião interna de 11/05 — ver [Ata 3](../atas/ata3_11_05_2026.md).
- Escopo redefinido após pivoteamento registrado na [Ata 2](../atas/ata2_04_05_2026.md): nova stack (FastAPI + MongoDB + Flutter + Streamlit) e replanejamento completo das histórias de usuário.

---

## Demonstração em Imagens

![Feed](../assets/Feed.png)

![Feed2](../assets/Feed2.png)

---

## Reuniões e Cerimônias Realizadas

### Sprint Planning

> Reunião de definição do escopo, estimativas e comprometimento do time para a sprint.

!!! success "Alinhamento Estratégico e Pivoteamento — 04/05/2026 · Presencial"

    --8<-- "atas/ata2_04_05_2026.md"

---

### Refinamento do User Story Map

> Reunião interna realizada na semana intermediária da sprint para revisão e detalhamento das histórias do User Story Map.

!!! info "Refinamento do User Story Map pós-pivoteamento — 05/05/2026 · Discord"

    --8<-- "atas/ata_refinamento_s2_05_05_2026.md"

---

### Validação com o Cliente

> Reunião de apresentação do incremento da sprint ao cliente para coleta de feedback e aprovação formal. Participantes: Letícia Vitória (equipe) e Paulo (stakeholder).

!!! success "Aprovação do Feed — 12/05/2026 · Discord · Letícia e Paulo"

    --8<-- "atas/ata4_12_05_2026.md"

---

### Retrospectiva da Equipe

> Percepções individuais dos membros sobre a sprint e aprendizados coletivos.

**Data:** _a preencher_  
**Participantes:** Davi Ursulino, João Leles, Letícia Vitória, Pedro Augusto e Pedro Druck

#### Comentários dos Membros

**Davi Ursulino**
> O pivoteamento foi a decisão certa e ficou evidente ao longo da sprint. A nova direção faz muito mais sentido para o produto. A dificuldade foi que, logo após a mudança, levamos um tempo para redistribuir as tarefas com clareza — mas superamos isso.

**João Leles**
> Foi um período de muita adaptação, mas saímos mais fortalecidos. O pivoteamento abriu nossa visão sobre o produto como um todo. A confusão inicial na definição do que cada um deveria fazer foi inevitável, porém foi superada ao longo da semana.

**Letícia Vitória**
> Essa sprint foi um marco para o projeto. O pivoteamento nos trouxe uma clareza que faltava na visão do produto. Logo após a reunião de mudança ficamos um pouco perdidos sobre como dividir o novo escopo, mas a equipe se reorganizou bem e entregamos o essencial.

**Pedro Augusto**
> Gostei muito da decisão de pivotar — ficou claro que era o caminho certo. A visão do time melhorou bastante depois disso. O único ponto negativo foi a confusão inicial para entender as novas responsabilidades dentro do novo escopo, o que custou alguns dias de replanejamento.

**Pedro Druck**
> O pivoteamento foi difícil de absorver no começo, mas foi necessário e muito positivo. Sair da reunião sabendo que tudo mudaria gerou uma certa ansiedade inicial. Com o tempo, a equipe se reorganizou bem e conseguimos entregar o CRUD do feed com boa qualidade.

#### Principais Aprendizados

- O pivoteamento realizado nesta sprint confirmou que mudanças de escopo e de arquitetura são inevitáveis quando as premissas iniciais não são suficientemente validadas com o cliente — replanejar o backlog completo com o cliente após a mudança foi essencial para realinhar as entregas.
- A curva de aprendizado do Flutter e do FastAPI é significativa: realizar provas de conceito e criar guias internos de padronização de endpoints (schemas, dependências) antes de avançar para implementações completas reduz ambiguidade e retrabalho na integração front-back.
- Construir e revisar o Story Map com o cliente ao longo das sprints garante alinhamento contínuo sobre o escopo e evita que o backlog fique desatualizado em relação às decisões técnicas e de negócio.
