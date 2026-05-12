# 8.1) Requisitos Funcionais (RF)

**Módulo Mobile (Público Geral)**
* Visualizar o histórico de doações e despesas da organização
* Visualizar publicações
* Filtrar publicações por tipo
* Buscar publicações por título
* Visualizar descrição e informações gerais da organização
* Visualizar oportunidades de voluntariado
* Contactar administradores da organização
* Inscrever-se para colaborar como voluntariado
* Inscrever-se para atender a um evento
* Realizar uma doação

**Módulo Administrativo**
* Autenticar um administrador 
* Cadastrar um administrador da organização 
* Remover administrador da organização 
* Configurar customização da organização 
* Lançar doação feita de forma externa ao aplicativo 
* Lançar despesa da organização
* Realizar uma publicação no feed 
* Atualizar uma publicação no feed
* Deletar uma publicação no feed 
* Registrar uma oportunidade de voluntariado 
* Atualizar uma oportunidade de voluntariado 
* Deletar uma oportunidade de voluntariado 

# 8.2) Requisitos Não Funcionais 

| Identificador | Nome | Descrição | Classificação |
| :--- | :--- | :--- | :--- |
| **RNF01** | Arquitetura Multi-tenant (White Label) | O back-end deve ser centralizado e exigir o envio de um hash de 32 dígitos (partition key) em cada requisição aos endpoints para identificar a qual organização os dados pertencem, sem necessidade de cadastro da organização via sistema convencional. | Restrição de Arquitetura (Sommerville) / Restrições de Design (URPS+) |
| **RNF02** | Parametrização de Interface e Configurações | A customização do aplicativo para cada organização (incluindo logo, nome, variáveis de tema da Ul e dados públicos institucionais) deve ser definida e consumida exclusivamente por meio de um arquivo JSON. | Restrição de Implementação (Sommerville) / Requisito de Implementação(URPS+) |
| **RNF03** | Interface de Administração em Streamlit | O painel administrativo para gestão da plataforma, conteúdo e transparência financeira deve ser desenvolvido utilizando a biblioteca Streamlit, acessado por meio de credenciais geradas previamente. | Restrição de Implementação (Sommerville) / Suportabilidade (FURPS+) |
| **RNF04** | Níveis de Acesso Administrativo | O módulo administrativo deve implementar um controle de acesso baseado em dois papéis hierárquicos rígidos: um "Administrador Geral" único (cujas credenciais são registradas diretamente no banco de dados, sem interface de cadastro público), que detém a permissão exclusiva de criar e gerenciar "Administradores da Organização". O papel de "Administrador da Organização" terá acesso total à gestão de conteúdo e finanças da organização, porém não terá permissões para provisionar novos administradores | Requisito de Segurança (Sommerville) / Segurança (FURPS+) |
| **RNF05** | Privacidade e Anonimato no Processamento de Doações | O fluxo de doação deve prover, antes do processo de pagamento, uma opção explícita para que o usuário decida se a sua contribuição será pública ou anônima. Caso opte pelo anonimato, o sistema (ao receber os dados via webhook do gateway externo) deve omitir automaticamente qualquer dado de identificação pessoal (como nome ou CPF) antes da persistência no banco de dados, garantindo que a doação conste na aba de transparência financeira apenas como "Doador Anônimo", em conformidade com as diretrizes de proteção de dados. | Requisito de Privacidade (Sommerville) / Segurança e Usabilidade (FURPS+) |
| **RNF06** | Integração com Gateway de Pagamento Externo | O processamento financeiro deve ser delegado a uma plataforma externa, e o back-end da aplicação deve confirmar a transação e receber as informações do doador (caso o doador não selecione que essa doação seja anônima) exclusivamente através da chamada de um webhook. Após isso, essa doação deve ser registrada automaticamente na parte de transparência. | Requisito de Interoperabilidade/Interface Externa (Sommerville) / Interface (FURPS+) |
| **RNF07** | Navegação e Estrutura de UI | A interface com o usuário no aplicativo móvel deve seguir uma estratégia visual organizada com três abas inferiores: Feed, Transparência e Colaboração, além de manter uma aba ou seção superior fixa para exibir as informações institucionais da organização. | Requisito de Usabilidade (Sommerville) / Usabilidade (FURPS+) |
| **RNF08** | Imutabilidade e Auditabilidade de Registros de Doações | O sistema deve garantir a imutabilidade, rastreabilidade e auditabilidade do histórico de doações realizadas através do aplicativo, utilizando a funcionalidade Object Retention Lock do Google Cloud Storage (GCS). Os registros devem ser armazenados no modelo WORM (Write Once, Read Many), impedindo qualquer alteração ou exclusão dos dados arquivados, com o objetivo de assegurar a validade jurídica e a conformidade para futuras auditorias da organização. | Requisito de Segurança (Sommerville) / Confiabilidade e Segurança (FURPS+) |
| **RNF09** | Classificação de uma Publicação do Feed | A estrutura de dados do feed deve suportar dois tipos de entidades de conteúdo: "Postagem Normal" (focada em atualizações institucionais, texto e mídia) e "Evento" (contendo metadados específicos como data, horário e local, além de uma opção para se inscrever). Na camada de interface com o usuário (front-end), sempre que uma publicação for tipada como "Evento", o sistema deve renderizar obrigatoriamente um componente interativo (Call to Action) acoplado à postagem, viabilizando a inscrição imediata do usuário na atividade sem que ele precise sair do contexto do feed. | Requisito de Domínio e Interface (Sommerville) / Usabilidade e Suportabilidade (FURPS+) |
| **RNF10** | Integração Externa para Ações de Engajamento e Contacto | Qualquer ação parte do utilizador final da aplicação mobile, que envolve o preenchimento de dados em um formulário, como por exemplo, a inscrição num evento, a candidatura a uma oportunidade de voluntariado ou o contacto direto com os administradores da organização, deve ser realizada exclusivamente através do redirecionamento para o preenchimento de um formulário externo (por exemplo, Google Forms, Typeform ou ferramentas equivalentes). O aplicativo móvel não deve processar ou armazenar os dados de inscrição internamente, atuando apenas como a interface que fornece a ligação (link/botão) para o ambiente externo da organização. | Requisito de Interoperabilidade/Interface Externa (Sommerville) / Interface e Suportabilidade (FURPS+) |
| **RNF11** | Destinação de Doações | O modelo de dados e o fluxo da interface de doação devem impor a seleção do destino do recurso como um parâmetro estrutural obrigatório antes da geração do pagamento no gateway externo. O sistema deve suportar uma alocação financeira de granularidade dupla, obrigando o usuário a definir se o valor será direcionado ao "Fundo Geral da Organização" ou a um "Projeto/Campanha Específica" cadastrado pelo administrador da organização. Essa escolha deve ser obrigatoriamente embutida nos metadados da requisição de pagamento, para que, ao ser devolvida via webhook, o sistema consiga categorizar e exibir o recurso corretamente no módulo de Transparência Financeira. | Requisito de Domínio (Sommerville) / Restrição de Design e Interface (FURPS+) |