
# Engenharia de Requisitos: Framework Ágil (Scrum/Kanban) para Plataforma de ONGs

Neste projeto, a Engenharia de Requisitos não é uma fase estática, mas um processo contínuo integrado ao **Product Backlog Refinement**. Utilizamos o **Scrum** para cadenciar as entregas em Sprints e o **Kanban** para garantir transparência e agilidade.

## 4.1 Atividades e Técnicas de ER

---

### Elicitação e Descoberta
O foco aqui é alimentar o Product Backlog de forma contínua, garantindo que as necessidades dos doadores e voluntários sejam capturadas em tempo real.

* **Lean Inception:** Realização de sessões rápidas para definir o MVP (Produto Mínimo Viável) do sistema, alinhando os objetivos de negócio logo no início do projeto.
* **User Stories (Histórias de Usuário):** Técnica principal para descrever funcionalidades sob o ponto de vista das personas (ex: Doador, Gestor de Ativos). Escritas no formato: *"Como [perfil], eu quero [ação] para que [valor/benefício]"*.
* **Backlog Refinement (Refinamento):** Reuniões periódicas envolvendo o time de desenvolvimento para detalhar histórias complexas (Epics) em itens menores e acionáveis para a próxima Sprint.

---

### Análise e Consenso
Envolve a priorização do que gera mais valor para a ONG e a resolução de dúvidas técnicas antes do início do desenvolvimento.

* **Estimativa de complexidade:** Uso da escala de fibonacci na plataforma Miro.
* **MoSCoW no Product Backlog:** Priorização dinâmica onde o PO define o que é essencial para o sucesso da ONG no curto prazo (*Must Have*) versus o que pode ser adiado.

---

### Declaração de Requisitos
Diferente de documentos extensos, a declaração aqui é viva e reside nas ferramentas de gestão visual.

* **Product Backlog:** A única fonte de verdade para os requisitos, mantida em uma ferramenta visual (Miro), contendo a descrição das User Stories.
* **Critérios de Aceite:** Cada requisito possui uma lista clara de condições que devem ser atendidas para que a funcionalidade seja aceita (ex: *"O sistema deve emitir recibo automático após a confirmação da doação"*).

---

### Representação de Requisitos
Foca na comunicação rápida e clara da interface e dos fluxos.

* **Protótipos de Baixa/Média Fidelidade:** Wireframes rápidos validados com o cliente para ajustar o fluxo de registro de assembleias e murais de notícias antes de qualquer linha de código.
* **User Story Mapping:** Representação visual da jornada do usuário pela plataforma, ajudando a visualizar como os sistemas de doação, patrimônio e voluntários se conectam para criar uma experiência completa.

---

### Verificação e Validação de Requisitos
A garantia de qualidade é feita através dos ritos do Scrum e das métricas do Kanban.

* **Definition of Ready (DoR):** Um requisito só entra na Sprint (Board Kanban) se estiver "Pronto": História escrita, Critérios de Aceite definidos, UI anexada e dependências técnicas resolvidas.
* **Definition of Done (DoD):** Garante a qualidade técnica. O requisito só é "Done" após passar por Code Review e alcançar todos os critérios de aceitação.
* **Sprint Review:** Reunião ao final de cada Sprint onde as funcionalidades entregues (ex: sistema de transparência) são validadas.

---

### Organização e Atualização de Requisitos
O Kanban garante que o fluxo de requisitos seja saudável e sem gargalos.

* **Quadro Kanban:** Visualização do status de cada requisito (Backlog, Em Análise, Pronto para Dev, Em Desenvolvimento, Concluído).
* **Feedback Contínuo:** Como as ONGs lidam com urgências sociais, o backlog é re-priorizado a cada Sprint para refletir mudanças súbitas nas necessidades de comunicação ou gestão de recursos.

## 4.2 Engenharia de Requisitos e o Processo Scrum/Kanban

As atividades de Engenharia de Requisitos (ER) foram integradas ao fluxo ágil, garantindo que a descoberta e a validação de necessidades sejam processos contínuos e adaptáveis.

| Fases do Scrum/Kanban | Atividades ER | Prática | Técnica | Resultado Esperado |
| :--- | :--- | :--- | :--- | :--- |
| **Fase 1: Discovery & Inception** | Elicitação e Descoberta | Alinhamento de Visão do Produto | Lean Inception | Atualização do MVP para os sistemas. |
| | Representação | Mapeamento da Jornada | User Story Mapping | Visão holística da conexão entre usuários e ONG's. |
| **Fase 2: Product Backlog Management** | Elicitação e Descoberta | Escrita de Requisitos Ágeis | User Stories (Personas) | Itens de backlog focados no valor para o usuário (ex: Doador). |
| | Declaração | Detalhamento de Requisitos | Critérios de Aceite | Regras claras para validação (ex: emissão automática de recibo). |
| | Organização e Atualização | Gestão Visual do Fluxo | Quadro Kanban (Backlog) | Transparência total sobre requisitos aguardando definição. |
| **Fase 3: Sprint Planning & Refinement** | Análise e Consenso | Estimativa e Priorização | Escala fibonacci e MoSCoW | Backlog da Sprint priorizado por valor de negócio. |
| | Verificação e Validação | Garantia de Prontidão | Definition of Ready (DoR) | Histórias com UI anexada e dependências técnicas resolvidas. |
| | Análise e Consenso | Refinamento Assistido | Prompt IA | Identificação de cenários de erro no sistema. |
| **Fase 4: Sprint Execution** | Representação | Prototipação Rápida | Wireframes (Baixa/Média) | Validação antes da codificação. |
| | Organização | Monitoramento de Entrega | Atualização | Agilidade na passagem do requisito de "To Do" para "Done". |
| **Fase 5: Sprint Review & Feedback** | Verificação e Validação | Homologação com Stakeholders | Sprint Review (Demo) | Validação das funcionalidades (ex: transparência). |
| | Verificação e Validação | Garantia de Qualidade | Definition of Done (DoD) | Requisito concluído após Code Review. |
