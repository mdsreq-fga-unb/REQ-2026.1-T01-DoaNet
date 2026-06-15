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
| **RF06** | Usuário | Feed de Post das Organizações | Filtrar publicações | **US06** Como usuário, quero filtrar as publicações do feed por tipo, para visualizar rapidamente atualizações ou eventos específicos. | RNF01, RNF10 |
| **RF07** | Usuário | Feed de Post das Organizações | Buscar publicações | **US07** Como usuário, quero buscar publicações por título, para localizar postagens de meu interesse. | RNF01 |
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

### Critérios de Aceitação

> Os critérios de aceitação e cenários BDD abaixo contemplam apenas as histórias de **Prioridade 1** e **Prioridade 2**, que entrarão em desenvolvimento imediato. As histórias de **Prioridade 3** terão seus critérios refinados quando forem promovidas para sprint.

---

#### Prioridade 1

##### US01 — Visualizar histórico financeiro

**Critérios de Aceitação**

- O sistema deve apresentar uma lista de registros de transações (doações e despesas).
- Cada registro deve exibir: data, valor e breve descrição.
- No caso de doações, o sistema deve sinalizar o destino ou campanha.
- Em caso de grande volume de dados, a interface deve implementar paginação ou carregamento contínuo (*lazy load*).

**Cenários BDD**

*Cenário 1 — Histórico com registros*

- **Dado** que o usuário acessa a aba de transparência
- **Quando** seleciona o histórico financeiro
- **Então** o sistema exibe doações e despesas ordenadas com descrição, data e valor

*Cenário 2 — Histórico vazio*

- **Dado** que a organização ainda não cadastrou registros financeiros
- **Quando** o usuário seleciona o histórico financeiro
- **Então** o sistema exibe mensagem informativa de que não há dados registrados

*Cenário 3 — Falha de conexão (Edge Case)*

- **Dado** que o usuário está sem conexão à internet
- **Quando** tenta acessar o histórico
- **Então** o sistema exibe mensagem de erro de conexão e oferece opção de tentar novamente

---

##### US02 — Visualizar publicações no feed

**Critérios de Aceitação**

- O feed da organização deve ser visível publicamente, sem necessidade de autenticação.
- As publicações devem ser exibidas em ordem cronológica decrescente (mais recentes primeiro).
- Publicações longas devem ser truncadas, com ação de "Ler mais" para expansão.

**Cenários BDD**

*Cenário 1 — Feed com publicações*

- **Dado** que o feed possui postagens da organização
- **Quando** o usuário acessa o feed
- **Então** visualiza a lista de publicações ordenadas da mais recente para a mais antiga

*Cenário 2 — Feed sem publicações (Edge Case)*

- **Dado** que a organização não realizou nenhuma publicação
- **Quando** o usuário acessa o feed
- **Então** o sistema exibe mensagem indicando que não há publicações no momento

---

##### US10 — Realizar doação

**Critérios de Aceitação**

- O doador deve selecionar obrigatoriamente o destino ou campanha da doação antes de prosseguir para o pagamento.
- O doador deve poder escolher se a doação será pública (exibindo seu nome) ou anônima.
- Erros do gateway de pagamento ou valores inválidos devem ser apresentados com mensagem amigável, mantendo o usuário na tela de pagamento.

**Cenários BDD**

*Cenário 1 — Doação pública com sucesso*

- **Dado** que o usuário informa o valor, seleciona o destino e escolhe visibilidade pública
- **Quando** confirma o pagamento e a transação é aprovada
- **Então** a doação é registrada e exibida com o nome do doador no painel de transparência

*Cenário 2 — Doação anônima com sucesso*

- **Dado** que o usuário informa o valor e seleciona visibilidade anônima
- **Quando** a transação é aprovada pelo gateway
- **Então** a doação é registrada como "Doador Anônimo" no painel de transparência

*Cenário 3 — Transação rejeitada (Edge Case)*

- **Dado** que o pagamento é recusado por fundos insuficientes ou cartão expirado
- **Quando** o gateway retorna falha na transação
- **Então** o sistema mantém o usuário na tela de pagamento e exibe mensagem explicativa do erro

---

##### US11 — Autenticar administradores

**Critérios de Aceitação**

- Após o login, o sistema deve exibir apenas os módulos correspondentes ao perfil do administrador ("Administrador Geral" ou "Administrador da Organização").
- Após exceder o limite de tentativas incorretas, a conta deve ser bloqueada temporariamente mesmo que a senha correta seja inserida em seguida.

**Cenários BDD**

*Cenário 1 — Login bem-sucedido*

- **Dado** que o administrador insere credenciais válidas
- **Quando** confirma o login
- **Então** o sistema concede acesso ao painel com os módulos correspondentes ao seu perfil hierárquico

*Cenário 2 — Bloqueio por excesso de tentativas (Edge Case)*

- **Dado** que um usuário tenta autenticar com credenciais incorretas repetidamente
- **Quando** atinge o limite configurado de tentativas malsucedidas
- **Então** o sistema bloqueia o acesso temporariamente e exibe mensagem orientando o usuário

---

##### US14 — Configurar dados institucionais (White Label)

**Critérios de Aceitação**

- O logotipo enviado deve ser um arquivo de imagem (PNG ou JPG) com no máximo 2 MB; arquivos fora desse padrão devem ser rejeitados com mensagem clara.
- Os valores de cor devem estar no formato hexadecimal válido (`#RRGGBB` ou `#RGB`); entradas inválidas devem ser apontadas antes do envio.

**Cenários BDD**

*Cenário 1 — Configuração bem-sucedida*

- **Dado** que o administrador insere um logotipo PNG abaixo de 2 MB e cores no formato hexadecimal válido
- **Quando** salva as configurações
- **Então** as alterações visuais são aplicadas ao aplicativo da organização

*Cenário 2 — Arquivo inválido ou muito pesado (Edge Case)*

- **Dado** que o administrador tenta enviar um arquivo com extensão incompatível ou acima do limite de tamanho
- **Quando** aciona o upload
- **Então** o sistema rejeita o arquivo e exibe mensagem indicando o motivo da rejeição

---

##### US15 — Lançar doações feitas externamente ao aplicativo

**Critérios de Aceitação**

- A data do registro não pode ser futura; deve ser igual ou anterior à data atual.
- Valor e descrição da doação são campos obrigatórios para o lançamento.

**Cenários BDD**

*Cenário 1 — Lançamento manual bem-sucedido*

- **Dado** que o administrador informa data retroativa, valor e descrição de uma doação recebida externamente
- **Quando** confirma o registro
- **Então** a doação aparece no painel de transparência financeira

*Cenário 2 — Data futura informada (Edge Case)*

- **Dado** que o administrador informa uma data de doação no futuro
- **Quando** tenta salvar o registro
- **Então** o sistema rejeita o lançamento e exibe aviso indicando que a data deve ser igual ou anterior à data atual

---

##### US17 — Criar publicação no feed

**Critérios de Aceitação**

- Título e corpo da publicação são campos obrigatórios, com limites mínimo e máximo de caracteres.
- Caso a publicação não seja enviada por falha de conexão, o sistema deve informar o erro e preservar o conteúdo redigido.

**Cenários BDD**

*Cenário 1 — Publicação criada com sucesso*

- **Dado** que o administrador preenche título e corpo com conteúdo dentro dos limites permitidos
- **Quando** confirma a criação
- **Então** a publicação aparece imediatamente no feed para todos os usuários

*Cenário 2 — Perda de conexão durante a redação (Edge Case)*

- **Dado** que o administrador redige uma publicação e a conexão é interrompida antes do envio
- **Quando** tenta publicar
- **Então** o sistema exibe aviso de falha de conexão e preserva o conteúdo redigido

---

#### Prioridade 2

##### US12 — Cadastrar novo administrador

**Critérios de Aceitação**

- O e-mail informado não pode já estar cadastrado no sistema (ativo ou inativo).
- A senha deve atender aos requisitos mínimos de força: pelo menos uma letra maiúscula, uma minúscula e um número.

**Cenários BDD**

*Cenário 1 — Cadastro bem-sucedido*

- **Dado** que o Administrador Geral informa um e-mail inédito e uma senha que atende aos requisitos
- **Quando** confirma o cadastro
- **Então** o novo administrador é criado e pode autenticar-se na plataforma

*Cenário 2 — E-mail já cadastrado (Edge Case)*

- **Dado** que o Administrador Geral informa um e-mail já existente no sistema
- **Quando** tenta salvar o novo cadastro
- **Então** o sistema rejeita o registro e exibe mensagem indicando que o e-mail já está em uso

---

##### US13 — Remover um administrador

**Critérios de Aceitação**

- O sistema deve impedir que um administrador remova a própria conta.
- A remoção deve ser precedida de confirmação em modal de dois passos para evitar exclusões acidentais.

**Cenários BDD**

*Cenário 1 — Remoção bem-sucedida*

- **Dado** que o Administrador Geral seleciona um administrador subordinado para exclusão
- **Quando** confirma a ação no modal de confirmação
- **Então** o acesso do administrador removido é revogado e ele não aparece mais na listagem

*Cenário 2 — Tentativa de auto-remoção (Edge Case)*

- **Dado** que o Administrador Geral tenta remover a própria conta
- **Quando** acessa a listagem de administradores
- **Então** o sistema oculta a opção de exclusão para a conta logada ou exibe erro de operação não permitida

---

#### Prioridade 3 — Critérios a detalhar

As histórias abaixo terão seus critérios de aceitação e cenários BDD refinados quando forem promovidas para sprint de desenvolvimento.

| US | Descrição |
| :--- | :--- |
| **US03** | Visualizar descrição da ONG |
| **US04** | Visualizar oportunidades de voluntariado |
| **US05** | Contactar a organização |
| **US06** | Filtrar publicações do feed |
| **US07** | Buscar publicações por título |
| **US08** | Inscrever-se para voluntariado |
| **US09** | Inscrever-se em eventos |
| **US16** | Lançar despesas operacionais |
| **US18** | Deletar uma publicação no feed |
| **US19** | Atualizar uma publicação no feed |
| **US20** | Registrar oportunidade de voluntariado |
| **US21** | Deletar oportunidade de voluntariado |
| **US22** | Atualizar oportunidade de voluntariado |

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

| US | Descrição | VN | CT | EI | ET | IP | Quadrante | Prioridade sugerida |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | 
| US11 | Autenticar administradores | 5 | 2 | 2 | 2 | 2,5 | Q1 Alto valor / Baixa carga técnica | Prioridade 1|
| US01 | Visualizar histórico financeiro | 5 | 2 | 2 | 2 | 2,5 | Q1 Alto valor / Baixa carga técnica | Prioridade 1 |
| US02 | Visualizar publicações | 5 | 2 | 2 | 2 | 2,5 | Q1 Alto valor / Baixa carga técnica | Prioridade 1 |
| US10 | Realizar doação | 5 | 2 | 2 | 2 | 2,5 | Q1 Alto valor / Baixa carga técnica | Prioridade 1 |
| US14 | Configurar dados institucionais | 4 | 2 | 2 | 2 | 2 | Q1 Alto valor / Baixa carga técnica | Prioridade 1 |
| US15 | Lançar doações e despesas | 4 | 2 | 2 | 2 | 2 | Q1 Alto valor / Baixa carga técnica | Prioridade 1 |
| US17 | Criar nova publicação no feed | 4 | 2 | 2 | 2 | 2 | Q1 Alto valor / Baixa carga técnica | Prioridade 1 |
| US12 | Cadastrar novo administrador | 5 | 4 | 4 | 4 | 1,25 |  Q2 Alto valor / Alta carga técnica | Prioridade 2 |
| US13 | Remover um administrador | 4 | 4 | 4 | 4 | 1 |  Q2 Alto valor / Alta carga técnica | Prioridade 2 |
| US03 | Visualizar descrição da ONG | 3 | 1 | 1 | 1 | 3 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 |
| US08 | Inscrever-se como voluntário | 3 | 2 | 2 | 2 | 1,5 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 |
| US09 | Inscrever-se em eventos | 3 | 2 | 2 | 2 | 1,5 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 |
| US16 | Lançar despesas operacionais | 3 | 2 | 2 | 2 | 1,5 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 |
| US19 | Atualizar uma publicação | 3 | 2 | 2 | 2 | 1,5 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 |
| US20 | Registrar oportunidade voluntariado | 3 | 2 | 2 | 2 | 1,5 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 |
| US22 | Atualizar oportunidade voluntariado | 3 | 2 | 2 | 2 | 1,5 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 |
| US06 | Filtrar publicações do feed | 2 | 2 | 2 | 2 | 1 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 |
| US07 | Buscar publicações por título | 2 | 2 | 2 | 2 | 1,5 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 |
| US04 | Visualizar oportunidades voluntariado | 2 | 2 | 2 | 2 | 1 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 |
| US05 | Contactar os administradores | 2 | 2 | 2 | 2 | 1 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 |
| US18 | Deletar uma publicação no feed | 2 | 2 | 2 | 2 | 1 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 |
| US21 | Deletar oportunidade voluntariado | 2 | 2 | 2 | 2 | 1 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 |