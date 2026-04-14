# 2. Solução Proposta  

## 2.1 Objetivo Geral  
O objetivo do produto é resolver a falta de informações claras sobre as Organizações da Sociedade Civil e a complexidade nos processos de pagamento ao centralizar a gestão e doações em uma plataforma que aumenta a visibilidade das organizações e promove a transparência e a confiança entre as partes.

## 2.2 Objetivos Específicos  
* **OE1:** Gerenciar doações e despesas.
* **OE2:** Exibir histórico financeiro.
* **OE3:** Cadastro de voluntários.
* **OE4:** Publicação de conteúdo.
* **OE5:** Administração do sistema.
* **OE6:** Gestão de eventos.
* **OE7:** Centralização de dados.
* **OE8:** Cadastro de organizações.

## 2.3 Características do Produto  

| ID | Funcionalidade | Descrição | Valor |
| :--- | :--- | :--- | :--- |
| **CP1** | Doações | Sistema via PIX | Facilidade |
| **CP2** | Transparência | Controle financeiro | Confiança |
| **CP3** | Feed | Comunicação | Engajamento |
| **CP4** | Voluntários | Gestão de equipe | Organização |
| **CP5** | Eventos | Inscrições | Participação |
| **CP6** | Perfil | Página pública | Visibilidade |
| **CP7** | Usuários | Controle de acesso | Segurança |
| **CP8** | Cadastro | Gestão de ONGs | Escala |

## 2.4 Tecnologias a Serem Utilizadas

Considerando as exigências arquiteturais e as características da solução proposta, o ecossistema tecnológico abaixo foi selecionado visando garantir escalabilidade, segurança e uma integração eficiente entre os serviços:

* *Python:* Linguagem de programação utilizada no desenvolvimento do back-end.
* *Django:* Usando no back-end o Django Rest Framework (DRF) para a construção de Api Rest.
* *PostgreSQL:* Banco de dados relacional.
* *Kafka:*  Apache Kafka será utilizado como um sistema para armazenar e gerenciar os eventos doações (em forma de log). O objetivo principal é fornecer uma maior auditabilidade das doações realizadas dentro do APP.
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