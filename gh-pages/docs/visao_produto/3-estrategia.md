# 3 Estratégias de Engenharia de Software

## 3.1 Estratégia Priorizada

- **Abordagem:** Híbrido
- **Ciclo de Vida:** Iterativo e Incremental
- **Processo:** Scrumban (Scrum + Kanban)

---

## 3.2 Quadro Comparativo

| Característica | Scrumban | OpenUP |
|---------------|--------------|-------------|
| **Abordagem geral** | Iterativo e incremental com foco em fluxo contínuo de trabalho e entregas frequentes com feedback contínuo. | Iterativo e incremental, com foco em entregas contínuas e evolução do produto. É uma versão mais leve do RUP. |
| **Foco em arquitetura** | Menor foco inicial na arquitetura, com evolução ao longo do tempo, conforme a necessidade e feedbacks dos usuários. | A arquitetura é definida nas fases iniciais, mas evolui ao longo do processo. Maior foco na definição de arquitetura do que em Scrum/Kanban. |
| **Estrutura de processos** | Baseado em sprints curtos (2-4 semanas) e um fluxo contínuo de trabalho (Kanban), com entregas frequentes e flexibilidade para mudanças no backlog. | Fase inicial de planejamento (Inception), seguida por uma fase de construção (Construction) e, finalmente, transição (Transition). Menos formal que o RUP. |
| **Flexibilidade de requisitos** | Alta flexibilidade para mudanças contínuas de requisitos a cada sprint, com adaptação rápida e feedback constante. | Alta flexibilidade com adaptação iterativa, mas exige que a arquitetura e requisitos principais sejam bem definidos nas fases iniciais. |
| **Colaboração com Cliente** | Colaboração constante com o cliente, com feedback ao final de cada sprint e ajustes rápidos nas funcionalidades conforme necessário. | Envolvimento contínuo do cliente, especialmente nas fases iniciais e finais de validação. Menos frequente que no Scrum. | 
| **Complexidade do Processo** | Leve e ágil, com menos formalidade e foco maior em entregas rápidas, sem tantas fases formais de planejamento. | Moderadamente complexo, com maior formalidade que o Scrum/Kanban, mas mais flexível que o RUP. Requer uma definição de papéis e tarefas de forma estruturada. |
| **Qualidade Técnica** | Foco contínuo em qualidade, com práticas como TDD, integração contínua, refatoração e feedback rápido, garantindo alta qualidade a cada entrega. | Garantida pela evolução da arquitetura e revisões incrementais ao longo do ciclo de vida do projeto. |
| **Práticas de Desenvolvimento** | Foco em fluxo de trabalho, limitação de tarefas em progresso (WIP), melhorias contínuas no processo e práticas ágeis (como TDD e integração contínua). | Foco em modelagem e arquitetura de software com práticas de controle de progresso e validação constante ao longo do processo. |
| **Adaptação ao Projeto da DoaNet** | Extremamente adequado para o projeto, já que ele permite evolução rápida e contínua da plataforma, com entregas incrementais e feedback direto da DoaNet. | Adequado, pois a flexibilidade do OpenUP permite que a arquitetura do sistema evolua conforme as necessidades do cliente, mas ainda com uma base sólida. |
| **Documentação** | Documentação mínima, com ênfase em comunicação constante e feedback rápido, apenas o necessário para o andamento do trabalho. | Exige documentação mais robusta e formal nas fases de Inception e Elaboration, mas de forma mais leve que o RUP. |
| **Controle de qualidade** | Controle contínuo de qualidade integrado ao processo de desenvolvimento com práticas como TDD, integração contínua e feedback constante. | Validação contínua do sistema com revisões incrementais e arquitetura em constante avaliação. |
| **Escalabilidade** | Escalável, mas mais indicado para equipes pequenas a médias, com comunicação direta e colaboração constante entre membros da equipe. | Pode ser escalado para projetos grandes, com múltiplas equipes e uma maior necessidade de planejamento e controle. |
| **Suporte a Equipes de Desenvolvimento** | Ideal para equipes menores e mais colaborativas, com maior flexibilidade e comunicação direta. | Suporta equipes de tamanho médio a grande, com papéis bem definidos e maior formalidade no processo. |

---

## 3.3 Justificativa

A partir das particularidades do projeto, e das dificuldades encontradas, o Scrumban é a escolha mais adequada, pelas seguintes características:

- **Flexibilidade e Adaptação Contínua:**
    Permite a adaptação contínua aos feedbacks do cliente e às mudanças de requisitos. Como o projeto DoaNet envolve uma plataforma digital para organizações da sociedade civil, as necessidades podem evoluir rapidamente à medida que a interação com os usuários (doadores, voluntários, administradores, etc.) cresce. O Scrumban permite que a equipe se adapte de forma ágil a essas mudanças, sem sobrecarregar o processo com planejamentos fixos ou fases rígidas.

- **Entregas Incrementais e Visibilidade Contínua:**
    O desenvolvimento é realizado em sprints curtos, semelhantes ao Scrum, mas com a flexibilidade do Kanban para ajustar o fluxo de trabalho de forma  contínua. Isso significa que a DoaNet poderá ter entregas regulares e incrementais, com visibilidade constante do progresso do projeto. A cada sprint ou  iteração, a plataforma será evoluída de forma tangível e com um feedback imediato da equipe e dos usuários, ajudando a validar rapidamente o impacto das mudanças implementadas.

- **Aumento da Eficiência no Uso de Recursos:**
    O Scrumban ajuda a reduzir desperdícios ao permitir que a equipe mantenha um fluxo constante de trabalho. O Kanban limita a quantidade de trabalho em andamento (WIP – Work In Progress), garantindo que a equipe não se sobrecarregue e que as tarefas sejam concluídas de maneira eficaz antes de começar novas tarefas. Isso ajuda a evitar multitarefas, que podem diminuir a eficiência da equipe e atrasar entregas importantes para a DoaNet. E devido ao tempo reduzido de desenvolvimento, e o tamanho enxuto da equipe, esse aumento da eficiência se torna ainda mais crucial.