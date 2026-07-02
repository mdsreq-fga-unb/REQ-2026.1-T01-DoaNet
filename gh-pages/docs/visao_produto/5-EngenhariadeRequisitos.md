# **5 ENGENHARIA DE REQUISITOS**

## **5.1 Atividades e Técnicas de ER**

***Elicitação e Descoberta:***

* **Entrevistas com Stakeholders:** No contexto do projeto, esta técnica será utilizada para captar o conhecimento de domínio e as necessidades reais dos administradores das organizações. Servirá para detalhar como os fluxos de Transparência Financeira e Gestão de Voluntários ocorrem na prática, garantindo que o módulo administrativo em Streamlit atenda a essas rotinas.
* **Brainstorming de Arquitetura e Produto:** Reuniões focadas em idear soluções técnicas e de produto para os desafios não funcionais mais críticos do sistema, como a estruturação da arquitetura *Multi-tenant* e o design do fluxo de privacidade e anonimato nas doações para atender as diretrizes de proteção de dados.

***Análise e Consenso:***

* **Priorização usando o gráfico Valor x Esforço:** Técnica aplicada em conjunto com o *Product Owner* (representando os interesses da ONG) para definir quais requisitos são críticos para o MVP e quais podem ficar para incrementos futuros, construindo um consenso sobre o escopo de cada *Sprint*.

***Declaração de Requisitos:***

* **Histórias de Usuário (User Stories) :** A principal forma de declarar requisitos no ScrumXP. Os requisitos funcionais serão descritos do ponto de vista do usuário final. 

***Representação de Requisitos:***

* **User Story Map:** Utilizado como a representação visual e estruturada de todas as necessidades do produto, organizando as Histórias de Usuário por jornada do usuário e prioridade de entrega. Permite à equipe e ao cliente visualizar o escopo completo do sistema, identificar o MVP e planejar as sprints de forma incremental e orientada ao valor.
* **Prototipação de UI / Wireframes:** Representação visual e interativa dos requisitos de interface e usabilidade. Será fundamental para materializar as exigências, desenhando e validando a estratégia das três abas inferiores (Feed, Transparência e Colaboração) e a exibição das informações institucionais antes da implementação do código *front-end*.

***Verificação e Validação de Requisitos:***

* **Critérios INVEST (Verificação):** Checklist aplicado durante o Sprint Planning para verificar se cada História de Usuário está bem formada antes de entrar na sprint. Cada US deve ser: **I**ndependente, **N**egociável, **V**aliosa, **E**stimável, **S**uficientemente pequena (*Small*) e **T**estável. Garante que o time só aceita itens que possuem informação suficiente para serem desenvolvidos com qualidade, alinhando-se diretamente ao DoR do projeto.
* **Protótipos e Feedback do Cliente (Validação):** Utilização dos protótipos de UI desenvolvidos no Figma como base para coleta de feedback direto do cliente nas reuniões de Revisão e Retrospectiva da Sprint. Permite validar se o incremento entregue atende às necessidades reais da organização antes de seguir para o próximo ciclo de desenvolvimento, conferindo rastreabilidade entre o que foi prototipado e o que foi implementado.

***Organização e Atualização de Requisitos:***

* **Refinamento do User Story Map:** Reunião interna realizada na semana intermediária de cada sprint, onde a equipe revisa e detalha as histórias de usuário pendentes, ajusta prioridades com base no progresso da sprint e atualiza o User Story Map com novos aprendizados técnicos e de produto — garantindo que as histórias da semana seguinte estejam bem formadas e estimadas antes de entrarem em desenvolvimento.

---

## **5.2 Engenharia de Requisitos e o ScrumXP**

| Fases do Processo (ScrumXP) | Atividades ER | Prática | Técnica | Resultado Esperado |
| :--- | :--- | :--- | :--- | :--- |
| **Planejamento da Release (Visão do Produto)** | Elicitação e Descoberta | Entendimento do Domínio de Negócio das ONGs | Entrevistas com Stakeholders e Brainstorming | Lista inicial de User Stories e levantamento macro das necessidades do app e painel administrativo. |
| **Planejamento da Release (Visão do Produto)** | Análise e Consenso | Estimativa em Equipe e Priorização de Escopo | Priorização Valor x Esforço | *User Story Map* inicial definido e esforço de desenvolvimento alinhado e aprovado pela equipe. |
| **Refinamento do User Story Map** | Declaração | Escrita Ágil e Focada no Usuário | Histórias de Usuário com Critérios de Aceitação | Histórias de usuário detalhadas, com critérios de aceite definidos e prontas para o desenvolvimento da semana seguinte. |
| **Refinamento do User Story Map** | Organização e Atualização | Revisão e Atualização Contínua do Mapa de Histórias | Refinamento do User Story Map | User Story Map atualizado com novos aprendizados, prioridades ajustadas e histórias futuras detalhadas. |
| **Refinamento do User Story Map** | Verificação de Requisitos | Checagem da Qualidade das Histórias de Usuário | Critérios INVEST | Histórias de Usuário verificadas e aprovadas para desenvolvimento: independentes, negociáveis, valiosas, estimáveis, pequenas e testáveis. |
| **Revisão e Retrospectiva da Sprint** | Validação de Requisitos | Demonstração do Incremento e Coleta de Feedback | Protótipos e Feedback do Cliente | Incremento validado pelo cliente com base no protótipo de referência; feedbacks registrados em ata e incorporados ao User Story Map da próxima sprint. |