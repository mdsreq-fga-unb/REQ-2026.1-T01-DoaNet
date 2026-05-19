# 8.1) Requisitos Funcionais (RF)

**Módulo Mobile (Público Geral)**

- RF01: Visualizar o histórico de doações e despesas da organização [CP2 - Painel de Transparência Financeira]

- RF02: Visualizar publicações no feed [CP3 - Feed de Comunicação]

- RF03: Visualizar uma descrição da organização [CP6 - Perfil Público da Organização]

- RF04: Visualizar oportunidades de voluntariado [CP4 - Gestão de Voluntários]

- RF05: Contactar administradores da organização [CP6 - Perfil Público da Organização]

- RF06: Filtrar publicações por tipo [CP3 - Feed de Comunicação]

- RF07: Buscar publicações por título [CP3 - Feed de Comunicação]

- RF08: Inscrever-se para colaborar como voluntariado [CP4 - Gestão de Voluntários]

- RF09: Inscrever-se para atender a um evento [CP5 - Gestão de Eventos]

- RF10: Realizar uma doação [CP1 - Sistema de Doações]

**Módulo Administrativo**

- RF11: Autenticar administradores [CP7 - Controle de Acesso Administrativo]

- RF12: Cadastrar um administrador da organização [CP7 - Controle de Acesso Administrativo]

- RF13: Remover administrador da organização [CP7 - Controle de Acesso Administrativos]

- RF14: Configurar dados de customização do aplicativo [CP8 - Customização da Organização]

- RF15: Lançar doação feita de forma externa ao aplicativo [CP2 - Sistema de Transparência Financeira]

- RF16: Lançar despesa da organização [CP2 - Sistema de Transparência Financeira]

- RF17: Realizar uma publicação no feed [CP3 - Feed de Comunicação]

- RF18: Deletar uma publicação no feed [CP3 - Feed de Comunicação]

- RF19: Atualizar uma publicação no feed [CP3 - Feed de Comunicação]

- RF20: Registrar uma oportunidade de voluntariado [CP4 - Gestão de Voluntários]

- RF21: Deletar uma oportunidade de voluntariado [CP4 - Gestão de Voluntários]

- RF22: Atualizar uma oportunidade de voluntariado [CP4 - Gestão de Voluntários]

# 8.2) Requisitos Não Funcionais 

| Identificador | Nome | Descrição | Classificação |
| :--- | :--- | :--- | :--- |
| **RNF01** | Arquitetura Multi-tenant (White Label) | O back-end deve ser centralizado e exigir o envio de um hash de 32 dígitos (partition key) em cada requisição aos endpoints para identificar a qual organização os dados pertencem, sem necessidade de cadastro da organização via sistema convencional. | Restrições de design |
| **RNF02** | Configuração e Costumização do Aplicativo | A customização do aplicativo para cada organização (incluindo logo, nome, variáveis de tema da Ul e dados públicos institucionais) deve ser definida e consumida exclusivamente por meio de um arquivo JSON. | Requisitos de Implementação |
| **RNF03** | Implementação das Diferentes Partes da Solução | O sistema deve ser implementado de ponta a ponta, com back-end em Python/FastAPI, banco de dados MongoDB, front-end em Flutter e painel administrativo em Streamlit, com versionamento no GitHub. | Requisitos de Implementação |
| **RNF04** | Níveis de Acesso Administrativo | O módulo administrativo deve implementar um controle de acesso baseado em dois papéis hierárquicos rígidos: um "Administrador Geral" único (cujas credenciais são registradas diretamente no banco de dados, sem interface de cadastro público), que detém a permissão exclusiva de criar e gerenciar "Administradores da Organização". O papel de "Administrador da Organização" terá acesso total à gestão de conteúdo e finanças da organização, porém não terá permissões para provisionar novos administradores. | Confiabilidade |
| **RNF05** | Privacidade e Anonimato no Processamento de Doações | O fluxo de doação deve prover, antes do processo de pagamento, uma opção explícita para que o usuário decida se a sua contribuição será pública ou anônima. Caso opte pelo anonimato, o sistema (ao receber os dados via webhook do gateway externo) deve omitir automaticamente qualquer dado de identificação pessoal (como nome ou CPF) antes da persistência no banco de dados, garantindo que a doação conste na aba de transparência financeira apenas como "Doador Anônimo", em conformidade com as diretrizes de proteção de dados. | Confiabilidade |
| **RNF06** | Integração com Gateway de Pagamento Externo | O processamento financeiro deve ser delegado a uma plataforma externa, e o back-end da aplicação deve confirmar a transação e receber as informações do doador (caso o doador não selecione que essa doação seja anônima) exclusivamente através da chamada de um webhook. Após isso, essa doação deve ser registrada automaticamente na parte de transparência. | Requisitos de Interface |
| **RNF07** | Navegação e Estrutura de UI | A interface com o usuário no aplicativo móvel deve seguir uma estratégia visual organizada com três abas inferiores: Feed, Transparência e Colaboração, além de manter uma aba ou seção superior fixa para exibir as informações institucionais da organização. | Usabilidade |
| **RNF08** | Garantia de Imutabilidade e Auditabilidade | O sistema deve garantir a imutabilidade, rastreabilidade e auditabilidade do histórico de doações, impedindo qualquer alteração ou exclusão dos dados arquivados para assegurar a validade jurídica e a conformidade para futuras auditorias da organização. | Confiabilidade |
| **RNF09** | Tecnologia de Armazenamento WORM (GCS) | Os registros imutáveis de doações devem ser armazenados no modelo WORM (Write Once, Read Many) utilizando obrigatoriamente a funcionalidade Object Retention Lock do Google Cloud Storage (GCS). | Requisitos de Implementação |
| **RNF10** | Classificação de uma Publicação do Feed | A estrutura de dados do feed deve suportar dois tipos de entidades de conteúdo: "Postagem Normal" e "Evento". Na camada de interface com o usuário, sempre que uma publicação for classificada como "Evento", o sistema deve renderizar um componente acoplado à postagem, que possibilite a inscrição para atender ao evento promovido na postagem. | Usabilidade |
| **RNF11** | Ações de Engajamento Dentro do Aplicativo | Qualquer ação do usuário no aplicativo que envolva o preenchimento de dados (confirmar presença em evento, voluntariado, contacto com a organização) deve ser realizada dentro do aplicativo, com formulários e envio de dados integrados à plataforma. | Funcionalidade |
| **RNF12** | Suporte para a Destinação de Doações | O sistema deve obrigar o usuário a selecionar e definir antes do pagamento, se o valor será direcionado ao "Fundo Geral da Organização" ou a um projeto/campanha específica (selecionada pelo usuário) cadastrada pelo administrador. Essa escolha deve ser obrigatoriamente embutida nos metadados da requisição de pagamento, para que, ao ser devolvida via webhook, o sistema consiga categorizar e exibir o recurso corretamente no módulo de Transparência Financeira.| Restrições de design |

# 8.3) Matriz-síntese de rastreabilidade

A matriz a seguir apresenta a rastreabilidade entre OE (Objetivos Específicos), CP (Características do Produto), VN (Valor de negócio), RF (Requisitos Funcionais) e RNF (Requisitos Não Funcionais).

| Contribuição principal | Contribuição secundária | **CP** (Características do Produto) | **VN** (Valor de negócio) | **RFs** relacionados (Requisitos Funcionais) | **RNFs** relacionados (Requisitos Não Funcionais) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **OE2** (Desburocratizar o processo de doação) | **OE3** (Fomentar a recorrência de contribuições) | **CP1** (Gestão de doações) | **VN1** (Facilitar o processo de doações e estabelecer confiança e credibilidade com a organização cadastrada) | **RF10** (Realizar uma doação) | **RNF01** (Arquitetura Multi-tenant (White Label)), **RNF05** (Privacidade e Anonimato no Processamento de Doações), **RNF06** (Integração com Gateway de Pagamento Externo), **RNF08** (Garantia de Imutabilidade e Auditabilidade), **RNF09** (Tecnologia de Armazenamento WORM (GCS)), **RNF12** (Suporte para a Destinação de Doações) |
| **OE1** (Aumentar a transparência financeira) | **OE5** (Ampliar a visibilidade do impacto social) | **CP2** (Painel de transparência financeira) | **VN2** (Transparência e prestação de contas) | **RF01** (Visualizar o histórico de doações e despesas da organização), **RF15** (Lançar doação feita de forma externa ao aplicativo), **RF16** (Lançar despesa da organização) | **RNF01** (Arquitetura Multi-tenant (White Label)), **RNF04** (Níveis de Acesso Administrativo), **RNF07** (Navegação e Estrutura de UI), **RNF08** (Garantia de Imutabilidade e Auditabilidade), **RNF09** (Tecnologia de Armazenamento WORM (GCS)) |
| **OE6** (Impulsionar o engajamento contínuo da comunidade) | **OE5** (Ampliar a visibilidade do impacto social) | **CP3** (Feed de comunicação) | **VN3** (Engajamento e visibilidade) | **RF02** (Visualizar publicações no feed), **RF06** (Filtrar publicações por tipo), **RF07** (Buscar publicações por título), **RF17** (Realizar uma publicação no feed), **RF18** (Deletar uma publicação no feed), **RF19** (Atualizar uma publicação no feed) | **RNF01** (Arquitetura Multi-tenant (White Label)), **RNF04** (Níveis de Acesso Administrativo), **RNF07** (Navegação e Estrutura de UI), **RNF10** (Classificação de uma Publicação do Feed) |
| **OE4** (Facilitar a captação e gestão de voluntários) | **OE7** (Otimizar acesso a informação) | **CP4** (Gestão de voluntários) | **VN4** (Organização de equipes de voluntários para uma organização) | **RF04** (Visualizar oportunidades de voluntariado), **RF08** (Inscrever-se para colaborar como voluntariado), **RF20** (Registrar uma oportunidade de voluntariado), **RF21** (Deletar uma oportunidade de voluntariado), **RF22** (Atualizar uma oportunidade de voluntariado) | **RNF01** (Arquitetura Multi-tenant (White Label)), **RNF04** (Níveis de Acesso Administrativo), **RNF07** (Navegação e Estrutura de UI), **RNF11** (Ações de Engajamento Dentro do Aplicativo) |
| **OE5** (Ampliar a visibilidade do impacto social) | **OE6** (Impulsionar o engajamento contínuo da comunidade) | **CP5** (Gestão de eventos) | **VN5** (Engajamento social e organização de participantes de eventos) | **RF09** (Inscrever-se para atender a um evento) | **RNF01** (Arquitetura Multi-tenant (White Label)), **RNF10** (Classificação de uma Publicação do Feed), **RNF11** (Ações de Engajamento Dentro do Aplicativo) |
| **OE5** (Ampliar a visibilidade do impacto social) | **OE1** (Aumentar a transparência financeira) | **CP6** (Perfil público da organização) | **VN6** (Visibilidade pública e centralização das informações relevantes de uma organização) | **RF03** (Visualizar uma descrição da organização), **RF05** (Contactar administradores da organização) | **RNF01** (Arquitetura Multi-tenant (White Label)), **RNF07** (Navegação e Estrutura de UI), **RNF11** (Ações de Engajamento Dentro do Aplicativo) |
| **OE7** (Otimizar acesso a informação) | **OE4** (Facilitar a captação e gestão de voluntários) | **CP7** (Controle de acesso administrativo) | **VN7** (Segurança e organização da plataforma) | **RF11** (Autenticar administradores), **RF12** (Cadastrar um administrador da organização), **RF13** (Remover administrador da organização) | **RNF01** (Arquitetura Multi-tenant (White Label)), **RNF04** (Níveis de Acesso Administrativo) |
| **OE5** (Ampliar a visibilidade do impacto social) | **OE7** (Otimizar acesso a informação) | **CP8** (Customização da Organização) | **VN8** (Fortalecer a identidade da marca perante o público e viabilizar a escalabilidade do sistema (White-Label)) | **RF14** (Configurar dados de customização do aplicativo) | **RNF01** (Arquitetura Multi-tenant (White Label)), **RNF02** (Configuração e Costumização do Aplicativo), **RNF04** (Níveis de Acesso Administrativo) |

