# 10 Story Map

## 10.1 User Story Map

A tabela a seguir apresenta cada um dos requisitos funcionais (RFs) declarados utilizando a técnica de *user story* (US), detalhando a **Persona**, o **Objetivo** e a **Atividade** correspondentes no *Story Map*, assim como a rastreabilidade com os requisitos não funcionais (RNFs).

| RF | Persona | Objetivo | Atividade | User Story derivada | RNFs relacionados |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **RF01** | Usuário | Transparência da organização | Visualizar histórico financeiro | [US01 - Visualizar histórico financeiro](../evidencias/sprint6.md#us01) | RNF01, RNF07, RNF08 |
| **RF02** | Usuário | Feed de Post das Organizações | Visualizar publicações | [US02 - Visualizar publicações no feed](../evidencias/sprint2.md#us02) | RNF01, RNF07, RNF10 |
| **RF03** | Usuário | Perfil geral da organização | Visualizar descrição da ONG | [US03 - Visualizar descrição da ONG](../evidencias/sprint6.md#us03) | RNF01, RNF07 |
| **RF04** | Usuário | Colaboração com a Organização | Visualizar voluntariado | [US04 - Visualizar oportunidades de voluntariado](../evidencias/sprint4.md#us04) | RNF01, RNF07 |
| **RF05** | Usuário | Perfil geral da organização | Contactar a organização | [US05 - Contactar a organização](../evidencias/sprint6.md#us05) | RNF01, RNF11 |
| **RF06** | Usuário | Feed de Post das Organizações | Restringir exibição do feed por categoria de publicação | [US06 - Filtrar publicações do feed](../evidencias/sprint5.md#us06) | RNF01, RNF10 |
| **RF07** | Usuário | Feed de Post das Organizações | Localizar publicação específica pelo título | [US07 - Buscar publicações por título](../evidencias/sprint5.md#us07) | RNF01 |
| **RF08** | Usuário | Colaboração com a Organização | Inscrever-se para voluntariado | [US08 - Inscrever-se como voluntário](../evidencias/sprint4.md#us08) | RNF01, RNF11 |
| **RF09** | Usuário | Colaboração com a Organização | Inscrever-se em eventos | [US09 - Inscrever-se em evento](../evidencias/sprint3.md#us09) | RNF01, RNF10, RNF11 |
| **RF10** | Usuário | Colaboração com a Organização | Realizar doação | [US10 - Realizar doação](../evidencias/sprint5.md#us10) | RNF01, RNF05, RNF06, RNF08, RNF09, RNF12 |
| **RF11** | Admin da organização / Admin geral | Gerenciar o funcionamento da organização | Autenticar administradores | [US11 - Autenticar administradores](../evidencias/sprint3.md#us11) | RNF01, RNF04 |
| **RF12** | Administrador geral | Gerenciar o funcionamento da organização | Gerenciar administradores | [US12 - Cadastrar administrador de organização](../evidencias/sprint6.md#us12) | RNF01, RNF04 |
| **RF13** | Administrador geral | Gerenciar o funcionamento da organização | Gerenciar administradores | [US13 - Remover administrador de organização](../evidencias/sprint6.md#us13) | RNF01, RNF04 |
| **RF14** | Administrador da organização | Perfil geral da organização | Configurar dados institucionais | [US14 - Configurar dados institucionais](../evidencias/sprint6.md#us14) | RNF01, RNF02, RNF04 |
| **RF15** | Administrador da organização | Transparência da organização | Lançar doações e despesas | [US15 - Lançar doações manuais](../evidencias/sprint5.md#us15) | RNF01, RNF04, RNF08, RNF09 |
| **RF16** | Administrador da organização | Transparência da organização | Lançar doações e despesas | [US16 - Lançar despesas operacionais](../evidencias/sprint5.md#us16) | RNF01, RNF04, RNF08 |
| **RF17** | Administrador da organização | Feed de Post das Organizações | Gerenciar publicações | [US17 - Criar publicação no feed](../evidencias/sprint2.md#us17) | RNF01, RNF04, RNF10 |
| **RF18** | Administrador da organização | Feed de Post das Organizações | Gerenciar publicações | [US18 - Deletar publicação no feed](../evidencias/sprint2.md#us18) | RNF01, RNF04 |
| **RF19** | Administrador da organização | Feed de Post das Organizações | Gerenciar publicações | [US19 - Atualizar publicação no feed](../evidencias/sprint2.md#us19) | RNF01, RNF04 |
| **RF20** | Administrador da organização | Colaboração com a Organização | Gestão de voluntários | [US20 - Registrar oportunidade de voluntariado](../evidencias/sprint4.md#us20) | RNF01, RNF04 |
| **RF21** | Administrador da organização | Colaboração com a Organização | Gestão de voluntários | [US21 - Deletar oportunidade de voluntariado](../evidencias/sprint4.md#us21) | RNF01, RNF04 |
| **RF22** | Administrador da organização | Colaboração com a Organização | Gestão de voluntários | [US22 - Atualizar oportunidade de voluntariado](../evidencias/sprint4.md#us22) | RNF01, RNF04 |


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
| [US11](../evidencias/sprint3.md#us11) | [Autenticar administradores](../evidencias/sprint3.md#us11) | 5 | 2 | 2 | 2 | 2,5 | Q1 Alto valor / Baixa carga técnica | Prioridade 1| X |
| [US01](../evidencias/sprint6.md#us01) | [Visualizar histórico financeiro](../evidencias/sprint6.md#us01) | 5 | 2 | 2 | 2 | 2,5 | Q1 Alto valor / Baixa carga técnica | Prioridade 1 | X |
| [US02](../evidencias/sprint2.md#us02) | [Visualizar publicações no feed](../evidencias/sprint2.md#us02) | 5 | 2 | 2 | 2 | 2,5 | Q1 Alto valor / Baixa carga técnica | Prioridade 1 | X |
| [US10](../evidencias/sprint5.md#us10) | [Realizar doação](../evidencias/sprint5.md#us10) | 5 | 2 | 2 | 2 | 2,5 | Q1 Alto valor / Baixa carga técnica | Prioridade 1 | X |
| [US14](../evidencias/sprint6.md#us14) | [Configurar dados institucionais](../evidencias/sprint6.md#us14) | 4 | 2 | 2 | 2 | 2 | Q1 Alto valor / Baixa carga técnica | Prioridade 1 | X |
| [US15](../evidencias/sprint5.md#us15) | [Lançar doações manuais](../evidencias/sprint5.md#us15) | 4 | 2 | 2 | 2 | 2 | Q1 Alto valor / Baixa carga técnica | Prioridade 1 | X |
| [US17](../evidencias/sprint2.md#us17) | [Criar publicação no feed](../evidencias/sprint2.md#us17) | 4 | 2 | 2 | 2 | 2 | Q1 Alto valor / Baixa carga técnica | Prioridade 1 | X |
| [US12](../evidencias/sprint6.md#us12) | [Cadastrar administrador de organização](../evidencias/sprint6.md#us12) | 5 | 4 | 4 | 4 | 1,25 |  Q2 Alto valor / Alta carga técnica | Prioridade 2 | X |
| [US13](../evidencias/sprint6.md#us13) | [Remover administrador de organização](../evidencias/sprint6.md#us13) | 4 | 4 | 4 | 4 | 1 |  Q2 Alto valor / Alta carga técnica | Prioridade 2 | X |
| [US03](../evidencias/sprint6.md#us03) | [Visualizar descrição da ONG](../evidencias/sprint6.md#us03) | 3 | 1 | 1 | 1 | 3 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 |
| [US08](../evidencias/sprint4.md#us08) | [Inscrever-se como voluntário](../evidencias/sprint4.md#us08) | 3 | 2 | 2 | 2 | 1,5 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 | X |
| [US09](../evidencias/sprint3.md#us09) | [Inscrever-se em evento](../evidencias/sprint3.md#us09) | 3 | 2 | 2 | 2 | 1,5 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 | X |
| [US16](../evidencias/sprint5.md#us16) | [Lançar despesas operacionais](../evidencias/sprint5.md#us16) | 3 | 2 | 2 | 2 | 1,5 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 |
| [US19](../evidencias/sprint2.md#us19) | [Atualizar publicação no feed](../evidencias/sprint2.md#us19) | 3 | 2 | 2 | 2 | 1,5 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 | X |
| [US20](../evidencias/sprint4.md#us20) | [Registrar oportunidade de voluntariado](../evidencias/sprint4.md#us20) | 3 | 2 | 2 | 2 | 1,5 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 | X |
| [US22](../evidencias/sprint4.md#us22) | [Atualizar oportunidade de voluntariado](../evidencias/sprint4.md#us22) | 3 | 2 | 2 | 2 | 1,5 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 | X |
| [US04](../evidencias/sprint4.md#us04) | [Visualizar oportunidades de voluntariado](../evidencias/sprint4.md#us04) | 2 | 2 | 2 | 2 | 1 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 | X |
| [US05](../evidencias/sprint6.md#us05) | [Contactar a organização](../evidencias/sprint6.md#us05) | 2 | 2 | 2 | 2 | 1 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 |
| [US18](../evidencias/sprint2.md#us18) | [Deletar publicação no feed](../evidencias/sprint2.md#us18) | 2 | 2 | 2 | 2 | 1 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 | X |
| [US21](../evidencias/sprint4.md#us21) | [Deletar oportunidade de voluntariado](../evidencias/sprint4.md#us21) | 2 | 2 | 2 | 2 | 1 | Q3 Baixo valor / Baixa carga técnica | Prioridade 3 | X |
| [US07](../evidencias/sprint5.md#us07) | [Buscar publicações por título](../evidencias/sprint5.md#us07) | 2 | 2 | 2 | 2 | 1,5 | Q4 Baixo valor / Baixa carga técnica | Prioridade 4 |
| [US06](../evidencias/sprint5.md#us06) | [Filtrar publicações do feed](../evidencias/sprint5.md#us06) | 2 | 2 | 2 | 2 | 1 | Q4 Baixo valor / Baixa carga técnica | Prioridade 4 |

