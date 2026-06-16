# 4 Estratégias de Engenharia de Software

## 4.1 Estratégia Priorizada

- **Abordagem:** Ágil
- **Ciclo de Vida:** Iterativo e Incremental
- **Processo de Desenvolvimento:** eXtreme Programming (XP) 
- **Framework de Gerenciamento:** Scrum 

---

## 4.2 Quadro Comparativo

| Característica | XP + Scrum (Estratégia Adotada) | OpenUP |
|--------------|--------------|-------------|
| **Características Gerais** | Abordagem Ágil com um ciclo de vida iterativo e incremental. Foca em adaptação contínua, entregas frequentes e excelência técnica na construção do código do projeto. | Abordagem Híbrida/Ágil com um ciclo de vida iterativo e incremental. Foca em equilibrar os requisitos com base em riscos e o valor que eles entregam (É uma versão ágil e mais leve do RUP) |
| **Foco em arquitetura** | A arquitetura e o design são construidos progressivamente e sempre que possível são mantidos simples, focando na refatoração contínua de código ao longo do tempo. | A arquitetura é o principal centro das decisões. É definida nas fases iniciais, com o objetivo de mitigar riscos técnicos de forma estruturada. |
| **Estrutura de processos** | Utiliza iterações de tempo fixo (*sprints*) com planejamento, revisão e retrospectiva. Sendo que o desenvolvimento segue com base no ritmo de entregas técnicas do XP. | Fase inicial de concepção (Inception), seguida por elaboração (Elaboration), construção (Construction) e transição (Transition), organizadas em micro-incrementos. |
| **Flexibilidade de requisitos** | Flexibilidade muito alta. Requisitos são muitas vezes variáveis e repriorizados facilmente a cada *sprint*. | Alta flexibilidade com adaptação iterativa, mas exige que a arquitetura e requisitos principais sejam bem definidos nas fases iniciais.|
| **Colaboração com Cliente** | Contínua e direta. Exige um alto envolvimento com cliente para feedbacks imediatos de validação ao final de cada *sprint* e, com base nisso, são feitos ajustes nas funcionalidades caso necessário. | Envolvimento contínuo do cliente especialmente nas fases iniciais, focado em validações nas entregas de iterações e acordo sobre a visão e arquitetura do sistema. Menos frequente que no Scrum. | 
| **Complexidade do Processo** | Mais leve e ágil, exigindo uma menor formalidade documental, porém precisa de uma maior disciplina técnica auto-organização e colaboração entre a equipe. | Moderadamente complexo. Com maior formalidade documental que o Scrum/XP, mas mais flexível que o RUP. Requer uma definição de papéis e tarefas de forma estruturada.|
| **Qualidade Técnica** | Foco principal na construção, garantido pelas práticas do XP: *Test-Driven Development* (TDD), integração contínua e refatoração. | Garantida pela evolução controlada da arquitetura e revisões incrementais ao longo do ciclo de vida do projeto. |
| **Práticas de Desenvolvimento** | Foco em práticas do desenvolvimento Ágil como a programação em pares (*pair programming*), design simples, TDD e integração contínua. | Foco em práticas de mitigação de riscos, desenvolvimento voltado a casos de uso, arquitetura baseada em componentes e validação do controle de progresso. |
| **Adaptação ao Projeto da DoaNet** | Extremamente adequada. O Scrum garante a organização em entregas curtas e repriorização rápida, enquanto o XP assegura o desenvolvimento de código testado e robusto desde o início até o fim do desenvolvimento do projeto. | Adequado, pois a flexibilidade do OpenUP permite que a arquitetura do sistema evolua conforme as necessidades do cliente, mas ainda com uma base sólida, porém a maior exigência formal pode gerar uma "burocracia" excessiva para uma equipe pequena. |
| **Documentação** | Minimaflista, pois a prioridade máxima é o software em funcionamento. A documentação é feita apenas quando agrega valor direto e é extremamente necessária. | Exige documentação mais robusta e formal nas fases de Inception e Elaboration, mas de forma mais leve que o RUP. |
| **Controle de qualidade** | Controle de qualidade preventivo e atrelado diretamente ao processo de desenvolvimento, através de testes automatizados e integração contínua do XP. | Validação contínua do sistema com revisões incrementais e arquitetura em constante avaliação. |
| **Escalabilidade** | Mais recomendado para equipes pequenas (como é o caso de nossa equipe). Pode ser escalado a projeto maiores, porém pode exigir uma futura adoção de frameworks baseados no Scrum mas focados em uma maior escala. | Pode ser escalado para projetos grandes, com múltiplas equipes e uma maior necessidade de planejamento e controle. |
| **Suporte a Equipes de Desenvolvimento** |Ideal para equipes de desenvolvimento menores, que possuam um foco em uma comunicação direta contínua e com alta capacidade de auto-organização. | Suporta equipes de tamanho médio a grande, com papéis bem definidos e maior formalidade no processo. |

---

## 4.3 Justificativa

A partir das particularidades do projeto DoaNet, a combinação do **Processo XP (eXtreme Programming)** com o **Framework Scrum** constitui a escolha mais eficaz, com base nas seguintes justificativas:

- **Complementaridade entre Processo e Framework:**
    A adoção do Scrum uma base gerencial (organização em sprints e papéis e cerimônias definidas), mas não especifica as práticas a serem seguidas na parte da programação. A inclusão do processo XP supre essa necessidade, fornecendo as práticas de engenharia de software rigorosas (desenvolvimento orientado a testes e refatoração).

- **Flexibilidade no Tratamento de Requisitos Variáveis:**
    O domínio da DoaNet envolve interações dinâmicas entre organizações civis, voluntários e doadores, e a abordagem ágil assume que os requisitos são naturalmente variáveis. A estrutura do Scrum/XP permite à equipe acomodar feedbacks contínuos e mudar as necessidades da plataforma sem ter o peso de uma maior exigência formal para realizar isso.

- **Foco e Eficiência Operacional em Equipe Enxuta:**
    A organização em sprints curtas estimula um ritmo de trabalho constante e com foco claro em metas de curto prazo. Além disso os princípios de design simples, minimizam falhas e retrabalhos. Dessa forma, maximizando a organização e produtividade da equipe.