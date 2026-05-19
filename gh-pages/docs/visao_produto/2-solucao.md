# 2. Solução Proposta  

## 2.1 Objetivo Geral  
O objetivo do produto é otimizar a gestão e a comunicação das ações e doações da MoveEduca por meio de uma plataforma unificada e transparente, que permita centralizar informações de impacto social e integrar os processos de doação, evitando dados dispersos e garantindo uma experiência de engajamento confiável para os usuários. A solução irá permitir à instituição fortalecer sua credibilidade e ampliar sua captação de recursos, assegurando que o sistema suporte o acompanhamento contínuo dos resultados à medida que a rede de doadores aumenta.

- **Observação:** Foi realizado um pivoteamento do projeto, que trouxe mudanças significativas, como o descontinuamento do Kafka, a utilização de um sistema externo para o processamento de pagamentos, além de ser definido que a doação poderá ser identificada ou anônima. Foram removidos os sistemas de login e cadastro para os usuários finais do aplicativo. Também será utilizado o Streamlit na administração, com acesso por meio de um login simples, pré-definido. Além disso iremos utilizar uma estratégia de white label para permitir a personalização da plataforma por diferentes organizações. E com relação a mudanças técnicas, trocamos o django pelo FastAPI, e o MySQL por MongoDB. Com base nessas mudanças, foram alterados os tópicos 2.2, 2.3, 2.4 e o 6.

## 2.2 Objetivos Específicos  
* **OE1: Aumentar a transparência financeira:** Garantir a rastreabilidade e a exposição clara da alocação de recursos, fortalecendo a confiança do público.
* **OE2: Desburocratizar o processo de doação:** Tornar a jornada de contribuição financeira mais fluida e intuitiva, reduzindo o atrito para novos doadores.
* **OE3: Fomentar a recorrência de contribuições:** Estabelecer canais de retorno e acompanhamento contínuo que incentivem doadores casuais a se tornarem apoiadores regulares.
* **OE4: Facilitar a captação e gestão de voluntários:** Simplificar o processo de adesão e alocação de pessoas interessadas em participar das iniciativas da instituição.
* **OE5: Ampliar a visibilidade do impacto social:** Centralizar a divulgação de ações, eventos e resultados, permitindo que a sociedade civil compreenda o alcance dos projetos.
* **OE6: Impulsionar o engajamento contínuo da comunidade:** Criar dinâmicas de interação que mantenham voluntários e o público geral ativamente conectados e participando das ações da organização a longo prazo.
* **OE7: Otimizar acesso a informação:** Unificar dados, comunicações e históricos em uma única plataforma, reduzindo o tempo gasto pela equipe com processos manuais e dispersos.

## 2.3 Características do Produto  

| ID | Característica do Produto (CP) | Descrição | Valor de Negócio (VN) | ID (VN) | Contribuição principal | Contribuição secundária |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **CP1** | Gestão de doações | Sistema de realização de doações (apenas via PIX) e registro dessas doações na plataforma. | Facilitar o processo de doações e estabelecer confiança e credibilidade com a organização cadastrada | VN1 | OE2 | OE3 |
| **CP2** | Painel de transparência financeira | Sistema de lançamento de doações recebidas dentro e fora da plataforma e de gastos feitos pela organização | Transparência e prestação de contas | VN2 | OE1 | OE5 |
| **CP3** | Feed de comunicação | Publicações, notícias e atualizações com mídia | Engajamento e visibilidade | VN3 | OE6 | OE5 |
| **CP4** | Gestão de voluntários | Cadastro, agendamento de turnos e controle de horas via formulário externo | Organização de equipes de voluntários para uma organização | VN4 | OE4 | OE7 | 
| **CP5** | Gestão de eventos | Divulgação e registro de participação em eventos via formulário externo | Engajamento social e organização de participantes de eventos | VN5 | OE5 | OE6 |
| **CP6** | Perfil público da organização | Página da organização cadastrada, onde estará presente as abas de feed, voluntários, eventos e transparência financeira | Visibilidade pública e centralização das informações relevantes de uma organização | VN6 | OE5 | OE1 |
| **CP7** | Controle de acesso administrativo | Perfis (admin/viewer) e controle de acesso | Segurança e organização da plataforma | VN7 | OE7 | OE4 | 
| **CP8** | Customização da Organização | Permite personalizar a identidade visual (logo, cores) e gerenciar os dados institucionais da organização na plataforma | Fortalecer a identidade da marca perante o público e viabilizar a escalabilidade do sistema (White-Label) | VN8 | OE5 | OE7 |

## 2.4 Tecnologias a Serem Utilizadas

Considerando as exigências arquiteturais e as características da solução proposta, o ecossistema tecnológico abaixo foi selecionado visando garantir escalabilidade, segurança e uma integração eficiente entre os serviços:

* *Python:* Linguagem de programação utilizada no desenvolvimento do back-end.
* *FastAPI:* Framework web moderno e de alto desempenho utilizado no back-end para a construção da API REST.
* *PostgreSQL:* Banco de dados relacional.
* *Flutter:* Framework multiplataforma adotado para o desenvolvimento do front-end e construção da interface com o usuário.
* *GitHub:* Repositório de integração contínua.

## 2.5 Pesquisa de Mercado e Análise Competitiva

Para o posicionamento do **DoaNet**, foram analisadas soluções reais que atendem ao terceiro setor. O foco foi identificar como essas ferramentas lidam com os problemas de visibilidade e gestão de recursos enfrentados por organizações como a **MoveEduca**.

### 2.5.1 Principais Soluções de Mercado (Foco em ONGs)

#### 2.5.1.1 Doare
A **Doare** é uma plataforma brasileira especializada em infraestrutura para doações. Ela oferece "páginas de doação" customizáveis e gestão de doadores recorrentes.
* **Foco:** Captação de recursos financeira e automação de pagamentos.
* **Limitação frente ao DoaNet:** Embora seja uma boa ferramenta para o controle do fluxo financeiro, ela não possui um ecossistema social integrado. Para gerir voluntários ou postar atualizações de projetos (feed), a ONG precisa contratar outras ferramentas externas, mantendo a fragmentação de dados.

#### 2.5.1.2 Atados
O **Atados** é a maior plataforma de voluntariado do Brasil, conectando pessoas que querem ajudar a causas sociais.
* **Foco:** Recrutamento e engajamento de voluntariado.
* **Limitação frente ao DoaNet:** O foco é estritamente humano/social. O Atados não oferece o suporte para gestão financeira e transparência de gastos, mantendo o problema da fragmentação de ferramentas.


---

### 2.5.2 Diferenciais Estratégicos do DoaNet

O DoaNet se diferencia por ser uma solução **híbrida e centralizadora**. Sendo os principais diferenciais:

#### 2.5.2.1. Unificação dos Ciclos de Engajamento e Doações
Enquanto o mercado oferece ferramentas separadas voltadas aos processos de engajamento e doação, o DoaNet integra ambos. No mesmo perfil onde o usuário possui a opção de realizar uma doação via PIX, ele pode se inscrever para um evento ou se candidatar a uma vaga de voluntário, criando um fluxo de engajamento contínuo.

#### 2.5.2.2 Redução de Silos Organizacionais
A solução resolve o problema dos "dados desorganizados e gestão desordenada" identificados no cenário atual. Ao centralizar finanças, comunicação e voluntariado em uma única interface administrativa, o DoaNet elimina a necessidade de múltiplas planilhas e sistemas obsoletos.

#### 2.5.2.3 Fortalecimento da Confiança (Trust-as-a-Service)
O diferencial tecnológico na segurança e rastreabilidade das informações financeiras ataca diretamente a "falta de confiança do público externo". O DoaNet não apenas facilita a doação, mas prova o impacto social gerado, por meio das funcionalidades de transparência incluidas na solução.

## 2.6 Viabilidade da Proposta

A proposta do projeto DoaNet é viável no contexto da disciplina, com um escopo dimensionado de forma realista para o prazo do semestre acadêmico. A equipe possui a maturidade e os conhecimentos técnicos prévios em desenvolvimento web necessários para a execução do software, além de uma divisão clara de papéis que evita a sobrecarga de trabalho. O contato direto e contínuo com o cliente (Paulo) garante a correta elicitação e validação constante dos requisitos. Com base nessa estrutura e priorizando as funcionalidades essenciais do sistema, a equipe tem plena capacidade de construir e entregar um Produto Mínimo Viável (MVP) funcional até o encerramento do projeto.

## 2.7 Benefícios Esperados

* Para o *cliente*: ampliar a capacidade de captação de recursos com maior controle financeiro e patrimonial, redução de riscos de erros contábeis e garantia de conformidade para auditorias. A solução também deverá fortalecer a credibilidade da organização perante parceiros e centralizar a gestão de sua memória institucional, voluntários e eventos 

* Para os *usuários*: uma experiência de engajamento social mais simples, transparente e confiável, com facilidade na realização e no rastreio de doações, navegação intuitiva pelo feed, podendo acessar o histórico da organização, comunicação centralizada sobre os impactos gerados, eventos e oportunidades de voluntariado.