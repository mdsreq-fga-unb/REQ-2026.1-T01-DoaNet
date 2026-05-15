# **5 ENGENHARIA DE REQUISITOS**

# 5 Engenharia de Requisitos: Framework Ágil (Scrum/Kanban) para Plataforma de ONGs

***Elicitação e Descoberta:***

## 5.1 Atividades e Técnicas de ER

---

## **5.2 Engenharia de Requisitos e o ScrumXP**

*Aqui, as atividades da ER, suas práticas e técnicas devem ser mapeadas, a partir das fases (etapas) do processo estabelecido pela equipe, para a condução do projeto. Essas informações devem ser apresentadas em uma tabela conforme indicado, a seguir.*

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

## 5.2 Engenharia de Requisitos e o Processo Scrum/Kanban

As atividades de Engenharia de Requisitos (ER) foram integradas ao fluxo ágil, garantindo que a descoberta e a validação de necessidades sejam processos contínuos e adaptáveis.

| Fases do Scrum/Kanban | Atividades ER | Prática | Técnica | Resultado Esperado |
| :--- | :--- | :--- | :--- | :--- |
| **Planejamento da Release (Visão do Produto)** | Elicitação e Descoberta | Entendimento do Domínio de Negócio das ONGs | Entrevistas com Stakeholders e Brainstorming | Lista inicial de User Stories e levantamento macro das necessidades do app e painel administrativo. |
| **Planejamento da Sprint (Sprint Planning)** | Análise e Consenso | Estimativa em Equipe e Priorização de Escopo | Priorização Valor x Esforço | *Sprint Backlog* definido e esforço de desenvolvimento alinhado e aprovado pela equipe. |
| **Planejamento da Sprint (Sprint Planning)** | Declaração | Escrita Ágil e Focada no Usuário | Histórias de Usuário com Critérios de Aceitação | Cartões de requisitos devidamente descritos, refinados e prontos para o desenvolvimento (XP). |
| **Execução da Sprint (Desenvolvimento XP)** | Organização e Atualização | Manutenção Contínua e Evolutiva dos Requisitos | Refinamento do Backlog | Backlog constantemente limpo, priorizado para a próxima iteração e com código rastreável. |
| **Revisão e Retrospectiva da Sprint** | Verificação e Validação | Demonstração do Produto e Garantia de Qualidade | Testes de Aceitação Automatizados | Incremento de software entregue, validado tecnicamente e aprovado pelas partes interessadas. |
