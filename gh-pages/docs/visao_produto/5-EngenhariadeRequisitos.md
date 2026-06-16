# **5 ENGENHARIA DE REQUISITOS**

## **5.1 Atividades e Técnicas de ER**

***Elicitação e Descoberta:***

* **Entrevistas com Stakeholders:** No contexto do projeto, esta técnica será utilizada para captar o conhecimento de domínio e as necessidades reais dos administradores das organizações. Servirá para detalhar como os fluxos de Transparência Financeira e Gestão de Voluntários ocorrem na prática, garantindo que o módulo administrativo em Streamlit atenda a essas rotinas.
* **Brainstorming de Arquitetura e Produto:** Reuniões focadas em idear soluções técnicas e de produto para os desafios não funcionais mais críticos do sistema, como a estruturação da arquitetura *Multi-tenant* e o design do fluxo de privacidade e anonimato nas doações para atender as diretrizes de proteção de dados.

***Análise e Consenso:***

* **Priorização usando o gráfico Valor x Esforço:** Técnica aplicada em conjunto com o *Product Owner* (representando os interesses da ONG) para definir quais requisitos são críticos para o MVP e quais podem ficar para incrementos futuros, construindo um consenso sobre o escopo de cada *Sprint*.

***Declaração de Requisitos:***

* **Histórias de Usuário (User Stories) com Critérios de Aceitação (XP):** A principal forma de declarar requisitos no ScrumXP. Os requisitos funcionais serão descritos do ponto de vista do usuário final. Os critérios de aceitação garantirão que restrições como renderização de componentes de eventos no feed (RNF10) sejam validadas.

***Representação de Requisitos:***

* **Product Backlog:** Utilizado como o repositório central e vivo de todas as necessidades do produto. Será gerenciado em ferramentas ágeis, ordenando os itens desde a implementação de ponta a ponta em FastAPI/MongoDB até os ajustes de interface do Flutter.
* **Prototipação de UI / Wireframes:** Representação visual e interativa dos requisitos de interface e usabilidade. Será fundamental para materializar as exigências, desenhando e validando a estratégia das três abas inferiores (Feed, Transparência e Colaboração) e a exibição das informações institucionais antes da implementação do código *front-end*.

***Verificação e Validação de Requisitos:***

* **Testes de Aceitação Automatizados (Prática XP):** Scripts criados para validar se os incrementos atendem rigorosamente aos Critérios de Aceitação declarados. Fundamental para verificar os RNFs que exigem alta confiabilidade, como a imutabilidade e rastreabilidade dos registros de doações (RNF08) e as regras rígidas de acesso hierárquico de administradores (RNF04).

***Organização e Atualização de Requisitos:***

* **Refinamento do Backlog:** Reuniões contínuas ao longo das Sprints onde a equipe técnica revisa as Histórias de Usuário futuras, dividindo tarefas grandes em entregas menores e atualizando requisitos baseados em novos aprendizados técnicos.

---

## **5.2 Engenharia de Requisitos e o ScrumXP**

*Aqui, as atividades da ER, suas práticas e técnicas devem ser mapeadas, a partir das fases (etapas) do processo estabelecido pela equipe, para a condução do projeto. Essas informações devem ser apresentadas em uma tabela conforme indicado, a seguir.*

| Fases do Processo (ScrumXP) | Atividades ER | Prática | Técnica | Resultado Esperado |
| :--- | :--- | :--- | :--- | :--- |
| **Planejamento da Release (Visão do Produto)** | Elicitação e Descoberta | Entendimento do Domínio de Negócio das ONGs | Entrevistas com Stakeholders e Brainstorming | Lista inicial de User Stories e levantamento macro das necessidades do app e painel administrativo. |
| **Planejamento da Sprint (Sprint Planning)** | Análise e Consenso | Estimativa em Equipe e Priorização de Escopo | Priorização Valor x Esforço | *Sprint Backlog* definido e esforço de desenvolvimento alinhado e aprovado pela equipe. |
| **Planejamento da Sprint (Sprint Planning)** | Declaração | Escrita Ágil e Focada no Usuário | Histórias de Usuário com Critérios de Aceitação | Cartões de requisitos devidamente descritos, refinados e prontos para o desenvolvimento (XP). |
| **Execução da Sprint (Desenvolvimento XP)** | Organização e Atualização | Manutenção Contínua e Evolutiva dos Requisitos | Refinamento do Backlog | Backlog constantemente limpo, priorizado para a próxima iteração e com código rastreável. |
| **Revisão e Retrospectiva da Sprint** | Verificação e Validação | Demonstração do Produto e Garantia de Qualidade | Testes de Aceitação Automatizados | Incremento de software entregue, validado tecnicamente e aprovado pelas partes interessadas. |