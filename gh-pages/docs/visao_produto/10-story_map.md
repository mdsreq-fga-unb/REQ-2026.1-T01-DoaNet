# 10 Story Map

## 10.1 User Story Map

A tabela a seguir apresenta cada um dos requisitos funcionais (RFs) declarados utilizando a técnica de *user story* (US), detalhando a **Persona**, o **Objetivo** e a **Atividade** correspondentes no *Story Map*, assim como a rastreabilidade com os requisitos não funcionais (RNFs).

| RF | Persona | Objetivo | Atividade | User Story derivada | RNFs relacionados |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **RF01** | Usuário | Transparência da organização | Visualizar histórico financeiro | **US01** Como usuário, quero visualizar o histórico de doações e despesas da organização, para acompanhar a transparência financeira de forma auditável. | RNF01, RNF07, RNF08 |
| **RF02** | Usuário | Feed de Post das Organizações | Visualizar publicações | **US02** Como usuário, quero visualizar as publicações no feed, para me manter atualizado sobre as ações e eventos da organização. | RNF01, RNF07, RNF10 |
| **RF03** | Usuário | Perfil geral da organização | Visualizar descrição da ONG | **US03** Como usuário, quero visualizar uma descrição institucional da organização, para entender seu propósito e áreas de atuação. | RNF01, RNF07 |
| **RF04** | Usuário | Colaboração com a Organização | Visualizar voluntariado | **US04** Como usuário, quero visualizar oportunidades de voluntariado, para encontrar vagas e formas de ajudar a ONG. | RNF01, RNF07 |
| **RF05** | Usuário | Perfil geral da organização | Contactar a organização | **US05** Como usuário, quero contactar os administradores da organização de forma integrada, para tirar dúvidas ou buscar mais informações. | RNF01, RNF11 |
| **RF06** | Usuário | Feed de Post das Organizações | Restringir exibição do feed por categoria de publicação | **US06** Como usuário, quero restringir a exibição do feed por tipo, para visualizar rapidamente atualizações ou eventos específicos. | RNF01, RNF10 |
| **RF07** | Usuário | Feed de Post das Organizações | Localizar publicação específica pelo título | **US07** Como usuário, quero localizar publicações por título, para localizar postagens de meu interesse. | RNF01 |
| **RF08** | Usuário | Colaboração com a Organização | Inscrever-se para voluntariado | **US08** Como usuário, quero me inscrever para colaborar como voluntário, para participar ativamente preenchendo meus dados dentro do próprio app. | RNF01, RNF11 |
| **RF09** | Usuário | Colaboração com a Organização | Inscrever-se em eventos | **US09** Como usuário, quero me inscrever para atender a um evento divulgado, para confirmar minha presença e participação. | RNF01, RNF10, RNF11 |
| **RF10** | Usuário | Colaboração com a Organização | Realizar doação | **US10** Como doador, quero realizar uma doação escolhendo seu direcionamento e visibilidade (pública/anônima), para apoiar financeiramente a causa. | RNF01, RNF05, RNF06, RNF08, RNF09, RNF12 |
| **RF11** | Admin da organização / Admin geral | Gerenciar o funcionamento da organização | Autenticar administradores | **US11** Como administrador, quero me autenticar na plataforma, para acessar o painel de gestão correspondente ao meu nível hierárquico. | RNF01, RNF04 |
| **RF12** | Administrador geral | Gerenciar o funcionamento da organização | Gerenciar administradores | **US12** Como Administrador Geral, quero cadastrar um novo administrador para uma organização, para provisionar seu acesso ao painel de gestão. | RNF01, RNF04 |
| **RF13** | Administrador geral | Gerenciar o funcionamento da organização | Gerenciar administradores | **US13** Como Administrador Geral, quero remover um administrador de organização, para revogar seu acesso e controle sobre o painel. | RNF01, RNF04 |
| **RF14** | Administrador da organização | Perfil geral da organização | Configurar dados institucionais | **US14** Como administrador da organização, quero configurar os dados de customização, para manter a interface do aplicativo alinhada ao branding da ONG (White Label). | RNF01, RNF02, RNF04 |
| **RF15** | Administrador da organização | Transparência da organização | Lançar doações e despesas | **US15** Como administrador da organização, quero lançar manualmente doações feitas fora do aplicativo, para centralizar e imortalizar os registros na transparência. | RNF01, RNF04, RNF08, RNF09 |
| **RF16** | Administrador da organização | Transparência da organização | Lançar doações e despesas | **US16** Como administrador da organização, quero lançar despesas operacionais, para prestar contas aos doadores publicamente. | RNF01, RNF04, RNF08 |
| **RF17** | Administrador da organização | Feed de Post das Organizações | Gerenciar publicações | **US17** Como administrador da organização, quero criar uma nova publicação no feed (normal ou evento), para me comunicar com os apoiadores. | RNF01, RNF04, RNF10 |
| **RF18** | Administrador da organização | Feed de Post das Organizações | Gerenciar publicações | **US18** Como administrador da organização, quero deletar uma publicação no feed, para remover um aviso incorreto ou que não seja mais pertinente. | RNF01, RNF04 |
| **RF19** | Administrador da organização | Feed de Post das Organizações | Gerenciar publicações | **US19** Como administrador da organização, quero atualizar uma publicação no feed, para corrigir ou adicionar detalhes importantes. | RNF01, RNF04 |
| **RF20** | Administrador da organização | Colaboração com a Organização | Gestão de voluntários | **US20** Como administrador da organização, quero registrar uma oportunidade de voluntariado, para divulgar vagas em aberto para os usuários. | RNF01, RNF04 |
| **RF21** | Administrador da organização | Colaboração com a Organização | Gestão de voluntários | **US21** Como administrador da organização, quero deletar uma oportunidade de voluntariado, para encerrar uma vaga já preenchida. | RNF01, RNF04 |
| **RF22** | Administrador da organização | Colaboração com a Organização | Gestão de voluntários | **US22** Como administrador da organização, quero atualizar uma oportunidade de voluntariado, para alterar requisitos ou o escopo da ajuda necessária. | RNF01, RNF04 |


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

## 10.3 Critérios de Aceite

Os critérios abaixo definem as condições mínimas que cada história de usuário deve satisfazer para ser considerada concluída. São verificados durante a revisão da sprint e servem de base para a validação com o cliente.

#### US01 — Visualizar histórico financeiro

- O histórico exibe doações e despesas em ordem cronológica decrescente.
- Cada registro apresenta tipo (doação/despesa), valor, data e descrição.
- O histórico é acessível sem autenticação pelo usuário comum.
- Os registros são imutáveis após lançamento — não podem ser editados ou excluídos.

#### US02 — Visualizar publicações no feed

- O feed exibe publicações em ordem cronológica decrescente.
- Cada publicação apresenta título, data de criação e imagem (quando disponível).
- O feed exibe tanto posts normais quanto posts de eventos.
- O feed é acessível sem autenticação.

#### US03 — Visualizar descrição da ONG

- A tela exibe nome, missão e descrição da organização.
- As informações refletem os dados configurados pelo administrador.
- A página é acessível sem autenticação.

#### US04 — Visualizar oportunidades de voluntariado

- A listagem exibe todas as oportunidades de voluntariado ativas.
- Cada oportunidade apresenta título, descrição e requisitos.
- A listagem é acessível sem autenticação.

#### US05 — Contactar os administradores

- O usuário acessa um canal de contato direto com a organização a partir da tela de perfil.
- O canal redireciona corretamente para o meio configurado (ex: WhatsApp, e-mail).

#### US06 — Filtrar publicações do feed

- O usuário consegue filtrar o feed por tipo de publicação (normal ou evento).
- O filtro é aplicado sem recarregar a tela.
- Ao remover o filtro, o feed retorna ao estado padrão com todas as publicações.

#### US07 — Buscar publicações por título

- O campo de busca filtra publicações em tempo real conforme o usuário digita.
- A busca não diferencia maiúsculas de minúsculas.
- Quando nenhum resultado é encontrado, uma mensagem informativa é exibida.

#### US08 — Inscrever-se como voluntário

- O formulário de inscrição coleta nome, contato e motivação do candidato.
- A inscrição é registrada e visível para o administrador no painel Streamlit.
- O usuário recebe confirmação visual após envio bem-sucedido.

#### US09 — Inscrever-se em evento

- O usuário consegue se inscrever em um evento a partir da publicação no feed.
- A inscrição é registrada e visível para o administrador.
- O usuário recebe confirmação visual após inscrição bem-sucedida.
- O sistema impede inscrição duplicada no mesmo evento.

#### US10 — Realizar doação

- O fluxo permite selecionar valor e direcionamento da doação.
- O doador escolhe entre visibilidade pública (nome exibido) ou anônima.
- O registro é imutável após confirmação do pagamento.
- A transação é processada por gateway de pagamento com criptografia.

#### US11 — Autenticar administradores

- O administrador consegue fazer login com credenciais válidas (e-mail + senha).
- Credenciais inválidas retornam mensagem de erro sem expor detalhes técnicos.
- Após autenticação, o painel exibe apenas as funcionalidades do nível hierárquico do admin.
- A sessão é encerrada após logout explícito.

#### US12 — Cadastrar novo administrador

- O administrador geral consegue cadastrar um novo admin informando nome, e-mail e organização vinculada.
- O novo administrador acessa o painel imediatamente com as credenciais criadas.
- O sistema impede o cadastro de dois administradores com o mesmo e-mail.

#### US13 — Remover um administrador

- O administrador geral consegue remover qualquer administrador de organização.
- O acesso do administrador removido é revogado imediatamente após a remoção.
- A remoção não afeta dados históricos criados pelo administrador removido.

#### US14 — Configurar dados institucionais

- O administrador consegue configurar nome, logotipo e cores da organização.
- As alterações são refletidas na interface do aplicativo em tempo real.
- Apenas administradores autenticados conseguem alterar os dados institucionais.

#### US15 — Lançar doações manuais

- O administrador consegue registrar uma doação informando valor, data e descrição.
- O registro é imediatamente visível no histórico de transparência para os usuários.
- O registro é imutável após confirmação — não pode ser editado ou excluído.

#### US16 — Lançar despesas operacionais

- O administrador consegue registrar uma despesa informando valor, data e categoria.
- O registro é imediatamente visível no histórico de transparência para os usuários.
- O registro é imutável após confirmação — não pode ser editado ou excluído.

#### US17 — Criar publicação no feed

- O administrador consegue criar uma publicação normal com título, texto e imagem opcional.
- O administrador consegue criar uma publicação de evento com título, texto, data do evento e imagem opcional.
- A publicação é exibida imediatamente no feed após criação.
- Apenas administradores autenticados conseguem criar publicações.

#### US18 — Deletar publicação no feed

- O administrador consegue excluir qualquer publicação do feed da sua organização.
- A publicação é removida imediatamente do feed após exclusão.
- Apenas administradores autenticados conseguem excluir publicações.

#### US19 — Atualizar publicação no feed

- O administrador consegue editar título, texto e imagem de uma publicação existente.
- As alterações são refletidas imediatamente no feed após salvar.
- Apenas administradores autenticados conseguem editar publicações.

#### US20 — Registrar oportunidade de voluntariado

- O administrador consegue criar uma oportunidade informando título, descrição e requisitos.
- A oportunidade é exibida imediatamente na listagem de voluntariado após criação.
- Apenas administradores autenticados conseguem registrar oportunidades.

#### US21 — Deletar oportunidade de voluntariado

- O administrador consegue excluir qualquer oportunidade de voluntariado da sua organização.
- A oportunidade é removida imediatamente da listagem após exclusão.
- Apenas administradores autenticados conseguem excluir oportunidades.

#### US22 — Atualizar oportunidade de voluntariado

- O administrador consegue editar título, descrição e requisitos de uma oportunidade existente.
- As alterações são refletidas imediatamente na listagem após salvar.
- Apenas administradores autenticados conseguem editar oportunidades.

---

### Sobre o MVP

A coluna **MVP** identifica as histórias de usuário selecionadas para compor o **Produto Mínimo Viável** do DoaNet — o conjunto mínimo de funcionalidades que entrega valor real ao usuário e à organização, validando as premissas centrais do produto.

A seleção foi feita com base no Índice de Prioridade (IP) calculado acima: foram incluídas no MVP as USs com maior relação valor de negócio / esforço técnico, priorizando os fluxos essenciais de cada módulo (feed, transparência, voluntariado e administração). As USs **sem marcação** no MVP representam incrementos futuros — funcionalidades de valor complementar que podem ser desenvolvidas após a validação do núcleo do produto com os usuários reais.
