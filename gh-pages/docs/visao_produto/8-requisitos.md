# 8.1) Requisitos Funcionais (RF)

**Módulo Mobile (Público Geral)**

- Visualizar o histórico de doações e despesas da organização

- Visualizar publicações

- Filtrar publicações por tipo

- Buscar publicações por título

- Visualizar descrição e informações gerais da organização

- Visualizar oportunidades de voluntariado

- Contactar administradores da organização

- Inscrever-se para colaborar como voluntariado

- Inscrever-se para atender a um evento

- Realizar uma doação

**Módulo Administrativo**

- Autenticar um administrador 

- Cadastrar um administrador da organização 

- Remover administrador da organização 

- Configurar customização da organização 

- Lançar doação feita de forma externa ao aplicativo 

- Lançar despesa da organização

- Realizar uma publicação no feed 

- Atualizar uma publicação no feed

- Deletar uma publicação no feed 

- Registrar uma oportunidade de voluntariado 

- Atualizar uma oportunidade de voluntariado 

- Deletar uma oportunidade de voluntariado 

# 8.2) Requisitos Não Funcionais 

| Identificador | Nome | Descrição | Classificação |
| :--- | :--- | :--- | :--- |
| **RNF01** | Arquitetura Multi-tenant (White Label) | O back-end deve ser centralizado e exigir o envio de um hash de 32 dígitos (partition key) em cada requisição aos endpoints para identificar a qual organização os dados pertencem, sem necessidade de cadastro da organização via sistema convencional. | Restrições de design |
| **RNF02** | Parametrização de Interface e Configurações | A customização do aplicativo para cada organização (incluindo logo, nome, variáveis de tema da Ul e dados públicos institucionais) deve ser definida e consumida exclusivamente por meio de um arquivo JSON. | Requisitos de Implementação |
| **RNF03** | Interface de Administração em Streamlit | O painel administrativo para gestão da plataforma, conteúdo e transparência financeira deve ser desenvolvido utilizando a biblioteca Streamlit, acessado por meio de credenciais geradas previamente. | Requisitos de Implementação |
| **RNF04** | Níveis de Acesso Administrativo | O módulo administrativo deve implementar um controle de acesso baseado em dois papéis hierárquicos rígidos: um "Administrador Geral" único (cujas credenciais são registradas diretamente no banco de dados, sem interface de cadastro público), que detém a permissão exclusiva de criar e gerenciar "Administradores da Organização". O papel de "Administrador da Organização" terá acesso total à gestão de conteúdo e finanças da organização, porém não terá permissões para provisionar novos administradores. | Confiabilidade |
| **RNF05** | Privacidade e Anonimato no Processamento de Doações | O fluxo de doação deve prover, antes do processo de pagamento, uma opção explícita para que o usuário decida se a sua contribuição será pública ou anônima. Caso opte pelo anonimato, o sistema (ao receber os dados via webhook do gateway externo) deve omitir automaticamente qualquer dado de identificação pessoal (como nome ou CPF) antes da persistência no banco de dados, garantindo que a doação conste na aba de transparência financeira apenas como "Doador Anônimo", em conformidade com as diretrizes de proteção de dados. | Confiabilidade |
| **RNF06** | Integração com Gateway de Pagamento Externo | O processamento financeiro deve ser delegado a uma plataforma externa, e o back-end da aplicação deve confirmar a transação e receber as informações do doador (caso o doador não selecione que essa doação seja anônima) exclusivamente através da chamada de um webhook. Após isso, essa doação deve ser registrada automaticamente na parte de transparência. | Requisitos de Interface |
| **RNF07** | Navegação e Estrutura de UI | A interface com o usuário no aplicativo móvel deve seguir uma estratégia visual organizada com três abas inferiores: Feed, Transparência e Colaboração, além de manter uma aba ou seção superior fixa para exibir as informações institucionais da organização. | Usabilidade |
| **RNF08** | Garantia de Imutabilidade e Auditabilidade | O sistema deve garantir a imutabilidade, rastreabilidade e auditabilidade do histórico de doações, impedindo qualquer alteração ou exclusão dos dados arquivados para assegurar a validade jurídica e a conformidade para futuras auditorias da organização. | Confiabilidade |
| **RNF09** | Tecnologia de Armazenamento WORM (GCS) | Os registros imutáveis de doações devem ser armazenados no modelo WORM (Write Once, Read Many) utilizando obrigatoriamente a funcionalidade Object Retention Lock do Google Cloud Storage (GCS). | Requisitos de Implementação |
| **RNF10** | Classificação de uma Publicação do Feed | A estrutura de dados do feed deve suportar dois tipos de entidades de conteúdo: "Postagem Normal" e "Evento". Na camada de interface com o usuário, sempre que uma publicação for tipada como "Evento", o sistema deve renderizar obrigatoriamente um componente interativo (Call to Action) acoplado à postagem, viabilizando a inscrição imediata na atividade sem sair do contexto do feed. | Usabilidade |
| **RNF11** | Integração Externa para Ações de Engajamento e Contacto | Qualquer ação do utilizador final que envolva o preenchimento de dados (inscrição num evento, voluntariado, contacto com a organização) deve ser realizada exclusivamente através do redirecionamento para um formulário externo (Google Forms, Typeform, etc.). O aplicativo móvel atuará apenas como a interface que fornece a ligação para este ambiente externo. | Requisitos de Interface |
| **RNF12** | Modelo de Dados para Destinação de Doações | O sistema deve suportar uma alocação financeira de granularidade dupla, obrigando o usuário a definir de forma estrutural, antes do pagamento, se o valor será direcionado ao "Fundo Geral da Organização" ou a um "Projeto/Campanha Específica" cadastrado pelo administrador. | Restrições de design |
| **RNF13** | Integração de Metadados de Pagamento | A escolha do destino do recurso feita pelo usuário deve ser obrigatoriamente embutida nos metadados da requisição de pagamento enviada ao gateway externo, para que, ao ser devolvida via webhook, o sistema consiga categorizar e exibir o recurso corretamente no módulo de Transparência Financeira. | Requisitos de Interface |