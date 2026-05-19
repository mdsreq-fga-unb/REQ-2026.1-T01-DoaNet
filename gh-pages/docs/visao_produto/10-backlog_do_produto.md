# 10 Backlog do Produto

## 10.1 Backlog Geral

A tabela a seguir apresenta cada um dos requisitos funcionais (RFs) declarados utilizando a técnica de *user story* (US), detalhando a **Persona**, o **Objetivo** e a **Atividade** correspondentes no *Story Map*, assim como a rastreabilidade com os requisitos não funcionais (RNFs).

| RF | Persona | Objetivo | Atividade | User Story derivada | RNFs relacionados | Critérios de Aceitação |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **RF01** | Usuário | Transparência da organização | Visualizar histórico financeiro | **US01** Como usuário, quero visualizar o histórico de doações e despesas da organização, para acompanhar a transparência financeira de forma auditável. | RNF01, RNF07, RNF08 | **DADO** que o usuário acessa a aba de transparência, **QUANDO** seleciona o histórico financeiro, **ENTÃO** o sistema exibe doações e despesas com data, valor, descrição e (no caso de doações) o destino. |
| **RF02** | Usuário | Feed de Post das Organizações | Visualizar publicações | **US02** Como usuário, quero visualizar as publicações no feed, para me manter atualizado sobre as ações e eventos da organização. | RNF01, RNF07, RNF10 | **DADO** que o feed está disponível, **QUANDO** o usuário acessa o feed, **ENTÃO** visualiza a lista de publicações ordenadas por data (mais recentes primeiro). |
| **RF03** | Usuário | Perfil geral da organização | Visualizar descrição da ONG | **US03** Como usuário, quero visualizar uma descrição institucional da organização, para entender seu propósito e áreas de atuação. | RNF01, RNF07 | **DADO** que o usuário acessa a aba de perfil da organização, **QUANDO** abre a seção de descrição, **ENTÃO** visualiza o texto institucional e as áreas de atuação. |
| **RF04** | Usuário | Colaboração com a Organização | Visualizar voluntariado | **US04** Como usuário, quero visualizar oportunidades de voluntariado, para encontrar vagas e formas de ajudar a ONG. | RNF01, RNF07 | **DADO** que o usuário acessa a aba de colaboração, **QUANDO** visualiza oportunidades, **ENTÃO** o sistema lista as vagas com seus detalhes. |
| **RF05** | Usuário | Perfil geral da organização | Contactar a organização | **US05** Como usuário, quero contactar os administradores da organização de forma integrada, para tirar dúvidas ou buscar mais informações. | RNF01, RNF11 | **DADO** que o usuário está no perfil da organização, **QUANDO** seleciona contactar, **ENTÃO** pode preencher o formulário de contato com os administradores e, quando enviar o formulário, notificar os administradores sobre a sua mensagem via email. |
| **RF06** | Usuário | Feed de Post das Organizações | Filtrar publicações | **US06** Como usuário, quero filtrar as publicações do feed por tipo, para visualizar rapidamente atualizações ou eventos específicos. | RNF01, RNF10 | **DADO** que o feed possui tipos de publicação, **QUANDO** o usuário aplica um filtro, **ENTÃO** o feed exibe apenas o tipo selecionado. |
| **RF07** | Usuário | Feed de Post das Organizações | Buscar publicações | **US07** Como usuário, quero buscar publicações por título, para localizar postagens de meu interesse. | RNF01 | **DADO** que o usuário está na tela do feed da organização e seleciona o filtro de busca por título, **QUANDO** informa um título e confirma, **ENTÃO** o sistema retorna publicações correspondentes. |
| **RF08** | Usuário | Colaboração com a Organização | Inscrever-se para voluntariado | **US08** Como usuário, quero me inscrever para colaborar como voluntário, para participar ativamente preenchendo meus dados dentro do próprio app. | RNF01, RNF11 | **DADO** que existe uma oportunidade de voluntariado aberta, **QUANDO** o usuário preenche os dados e confirma, **ENTÃO** a inscrição é registrada e confirmada. |
| **RF09** | Usuário | Colaboração com a Organização | Inscrever-se em eventos | **US09** Como usuário, quero me inscrever para atender a um evento divulgado, para confirmar minha presença e participação. | RNF01, RNF10, RNF11 | **DADO** que um evento está publicado, **QUANDO** o usuário confirma presença e envia seus dados, **ENTÃO** a inscrição no evento é registrada. |
| **RF10** | Usuário | Colaboração com a Organização | Realizar doação | **US10** Como doador, quero realizar uma doação escolhendo seu direcionamento e visibilidade (pública/anônima), para apoiar financeiramente a causa. | RNF01, RNF05, RNF06, RNF08, RNF09, RNF12 | **DADO** que o usuário está na tela de doação, **QUANDO** escolhe destino, visibilidade de nome e confirma o pagamento, **ENTÃO** a doação é registrada com essas escolhas. |
| **RF11** | Admin da organização / Admin geral | Gerenciar o funcionamento da organização | Autenticar administradores | **US11** Como administrador, quero me autenticar na plataforma, para acessar o painel de gestão correspondente ao meu nível hierárquico. | RNF01, RNF04 | **DADO** que o administrador possui credenciais válidas, **QUANDO** realiza login, **ENTÃO** o painel correspondente ao seu perfil é exibido. |
| **RF12** | Administrador geral | Gerenciar o funcionamento da organização | Gerenciar administradores | **US12** Como Administrador Geral, quero cadastrar um novo administrador para uma organização, para provisionar seu acesso ao painel de gestão. | RNF01, RNF04 | **DADO** que o Administrador Geral está autenticado, **QUANDO** cadastra um novo administrador com dados obrigatórios, **ENTÃO** o acesso é criado e habilitado. |
| **RF13** | Administrador geral | Gerenciar o funcionamento da organização | Gerenciar administradores | **US13** Como Administrador Geral, quero remover um administrador de organização, para revogar seu acesso e controle sobre o painel. | RNF01, RNF04 | **DADO** que o Administrador Geral seleciona um administrador, **QUANDO** confirma a remoção, **ENTÃO** o acesso desse administrador é revogado. |
| **RF14** | Administrador da organização | Perfil geral da organização | Configurar dados institucionais | **US14** Como administrador da organização, quero configurar os dados de customização, para manter a interface do aplicativo alinhada ao branding da ONG (White Label). | RNF01, RNF02, RNF04 | **DADO** que o administrador da organização está no painel, **QUANDO** atualiza logo, cores e nome, **ENTÃO** o aplicativo reflete a nova identidade visual. |
| **RF15** | Administrador da organização | Transparência da organização | Lançar doações e despesas | **US15** Como administrador da organização, quero lançar manualmente doações feitas fora do aplicativo, para centralizar e imortalizar os registros na transparência. | RNF01, RNF04, RNF08, RNF09 | **DADO** que o administrador da organização preenche os dados da doação externa, **QUANDO** confirma o lançamento, **ENTÃO** o registro aparece na aba de transparência. |
| **RF16** | Administrador da organização | Transparência da organização | Lançar doações e despesas | **US16** Como administrador da organização, quero lançar despesas operacionais, para prestar contas aos doadores publicamente. | RNF01, RNF04, RNF08 | **DADO** que o administrador da organização preenche os dados da despesa, **QUANDO** confirma o lançamento, **ENTÃO** a despesa aparece na aba de transparência. |
| **RF17** | Administrador da organização | Feed de Post das Organizações | Gerenciar publicações | **US17** Como administrador da organização, quero criar uma nova publicação no feed (normal ou evento), para me comunicar com os apoiadores. | RNF01, RNF04, RNF10 | **DADO** que o administrador cria uma publicação com título e conteúdo, **QUANDO** salva, **ENTÃO** a publicação aparece no feed conforme o tipo escolhido. |
| **RF18** | Administrador da organização | Feed de Post das Organizações | Gerenciar publicações | **US18** Como administrador da organização, quero deletar uma publicação no feed, para remover um aviso incorreto ou que não seja mais pertinente. | RNF01, RNF04 | **DADO** que o administrador seleciona uma publicação, **QUANDO** confirma a exclusão, **ENTÃO** ela deixa de aparecer no feed. |
| **RF19** | Administrador da organização | Feed de Post das Organizações | Gerenciar publicações | **US19** Como administrador da organização, quero atualizar uma publicação no feed, para corrigir ou adicionar detalhes importantes. | RNF01, RNF04 | **DADO** que o administrador edita uma publicação existente, **QUANDO** salva as alterações, **ENTÃO** o feed exibe os dados atualizados. |
| **RF20** | Administrador da organização | Colaboração com a Organização | Gestão de voluntários | **US20** Como administrador da organização, quero registrar uma oportunidade de voluntariado, para divulgar vagas em aberto para os usuários. | RNF01, RNF04 | **DADO** que o administrador registra uma oportunidade com requisitos e período, **QUANDO** salva, **ENTÃO** ela aparece na aba de colaboração. |
| **RF21** | Administrador da organização | Colaboração com a Organização | Gestão de voluntários | **US21** Como administrador da organização, quero deletar uma oportunidade de voluntariado, para encerrar uma vaga já preenchida. | RNF01, RNF04 | **DADO** que o administrador seleciona uma oportunidade, **QUANDO** confirma a exclusão, **ENTÃO** ela deixa de ser exibida na colaboração. |
| **RF22** | Administrador da organização | Colaboração com a Organização | Gestão de voluntários | **US22** Como administrador da organização, quero atualizar uma oportunidade de voluntariado, para alterar requisitos ou o escopo da ajuda necessária. | RNF01, RNF04 | **DADO** que o administrador atualiza uma oportunidade existente, **QUANDO** salva, **ENTÃO** os novos detalhes aparecem na colaboração. |

> **Observação:** O **RNF03** (Implementação das Diferentes Partes da Solução usando Python/FastAPI, Flutter e MongoDB) aplica-se transversalmente a todas as características do produto, requisitos funcionais e user stories, por definir a base tecnológica e o padrão arquitetural do projeto. Assim, ele deve ser considerado válido para todo o escopo do backlog.

## 10.2 Priorização do Backlog e MVP

Para a priorização foram utilizados os seguintes critérios:

- **VN** = Valor de negócio (1 a 5)

    - **O que significa:** O impacto positivo que a funcionalidade traz para a organização (ONG) ou para o usuário final. Mede o quanto aquela entrega resolve uma dor real, gera engajamento, traz segurança jurídica/financeira ou atende ao objetivo central do aplicativo.

    - **Como mensurar:**

        - **1 a 2 (Baixo):** Recursos cosméticos, relatórios secundários ou funções que poucos usuários vão usar.

        - **3 (Médio):** Funcionalidades de suporte importantes, mas que não impedem a operação principal se estiverem    ausentes.

        - **4 a 5 (Alto):** Funcionalidades críticas e core do sistema (Ex: Autenticação de admins, realização de doações,    transparência financeira). Sem elas, o produto perde o propósito.

- **CT** = Complexidade técnica (1 a 5)

    - **O que significa:** O nível de dificuldade intelectual, incerteza, novidade ou risco envolvido no desenvolvimento da história. Avalia se a equipe já sabe como fazer ou se exigirá muita pesquisa, integrações com terceiros (APIs externas) ou arquiteturas robustas.

    - **Como mensurar:**

        - **1 a 2 (Baixo):** Telas estáticas, cadastros simples (CRUDs) e comportamentos que a equipe já domina amplamente.

        - **3 (Médio):** Regras de negócio moderadas, filtros dinâmicos ou consultas que exigem maior atenção na modelagem.

        - **4 a 5 (Alto):** Recursos que envolvem criptografia, gateway de pagamento externo, regras de White Label dinâmicas ou alta exigência de segurança e performance.

- **EI** = Esforço de implementação (1 a 5)

    - **O que significa:** O volume de trabalho bruto e o tempo necessário para codificar, testar e homologar a funcionalidade. Uma tarefa pode ser conceitualmente simples (baixa complexidade), mas muito repetitiva ou longa (alto esforço).

    - **Como mensurar:**

        - **1 a 2 (Baixo):** Alterações rápidas, mensagens de erro, criação de botões ou fluxos de cliques curtos.

        - **3 (Médio):** Desenvolvimento padrão que consome alguns dias de trabalho de um desenvolvedor focado.

        - **4 a 5 (Alto):** Fluxos longos que exigem muitas telas, validações extensas de dados, e cenários complexos de testes manuais ou automatizados.


### 1. Esforço Técnico

Para metrificar o esforço técnico como um todo, utilizamos:

**ET = (CT + EI)/2**

Escala continua de 1 a 5.

### 2. Indice de prioridade

Para calcular o indice de prioridade:

**IP = VN / ET**

Quanto maior for o valor do IP, maior a priodade.

Sendo:

- **IP Alto** = alto valor de negócio para baixo custo técnico
- **IP Médio** = Equilibrio entre valor de negócio e custo técnico
- **IP Baixo** = pouco valor de negócio para alto custo técnico

A partir dessas informações, foi gerada a seguinte tabela:

| US | Descrição | VN | CT | EI | ET | IP | Quadrante | Prioridade sugerida | MVP |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |  :--- |
| US11 | Autenticar administradores | 5 | 2 | 2 | 2 | 2,5 | Q1 Alto valor / Baixa carga técnica | Prioridade 1| X |
| US01 | Visualizar histórico financeiro | 5 | 2 | 2 | 2 | 2,5 | Q1 Alto valor / Baixa carga técnica | Prioridade 1 | X |
| US02 | Visualizar publicações | 5 | 2 | 2 | 2 | 2,5 | Q1 Alto valor / Baixa carga técnica | Prioridade 1 | X |
| US10 | Realizar doação | 5 | 2 | 2 | 2 | 2,5 | Q1 Alto valor / Baixa carga técnica | Prioridade 1 | X |
| US14 | Configurar dados institucionais | 4 | 2 | 2 | 2 | 2 | Q1 Alto valor / Baixa carga técnica | Prioridade 1 | X |
| US15 | Lançar doações e despesas | 4 | 2 | 2 | 2 | 2 | Q1 Alto valor / Baixa carga técnica | Prioridade 1 | X |
| US17 | Criar nova publicação no feed | 4 | 2 | 2 | 2 | 2 | Q1 Alto valor / Baixa carga técnica | Prioridade 1 | X |
| US12 | Cadastrar novo administrador | 5 | 4 | 4 | 4 | 1,25 |  Q2 Alto valor / Alta carga técnica | Prioridade 2 | X |
| US13 | Remover um administrador | 4 | 4 | 4 | 4 | 1 |  Q2 Alto valor / Alta carga técnica | Prioridade 2 | X |
| US03 | Visualizar descrição da ONG | 3 | 1 | 1 | 1 | 3 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 |
| US08 | Inscrever-se como voluntário | 3 | 2 | 2 | 2 | 1,5 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 | X |
| US09 | Inscrever-se em eventos | 3 | 2 | 2 | 2 | 1,5 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 | X |
| US16 | Lançar despesas operacionais | 3 | 2 | 2 | 2 | 1,5 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 |
| US19 | Atualizar uma publicação | 3 | 2 | 2 | 2 | 1,5 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 | X |
| US20 | Registrar oportunidade voluntariado | 3 | 2 | 2 | 2 | 1,5 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 | X |
| US22 | Atualizar oportunidade voluntariado | 3 | 2 | 2 | 2 | 1,5 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 | X |
| US04 | Visualizar oportunidades voluntariado | 2 | 2 | 2 | 2 | 1 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 | X |
| US05 | Contactar os administradores | 2 | 2 | 2 | 2 | 1 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 |
| US18 | Deletar uma publicação no feed | 2 | 2 | 2 | 2 | 1 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 | X |
| US21 | Deletar oportunidade voluntariado | 2 | 2 | 2 | 2 | 1 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 | X |
| US07 | Buscar publicações por título | 2 | 2 | 2 | 2 | 1,5 | Q4 Baixo valor / Baixa carga técnica | Prioridade 4 |
| US06 | Filtrar publicações do feed | 2 | 2 | 2 | 2 | 1 | Q4 Baixo valor / Baixa carga técnica | Prioridade 4 |