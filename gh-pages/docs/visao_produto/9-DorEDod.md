# 9 - DoR e DoD

## 9.1 Definition of Ready (DoR)

O DoR é um acordo entre o time e o Product Owner (PO) indicando quando um requisito estará preparado para ser puxado para uma Sprint. Alguns itens que podem ser verificados para determinar se um requisito está 'Ready' são:

* **O requisito possui informação necessária para ser trabalhado?**
  O requisito deve ter detalhes suficientes para que o time de desenvolvimento entenda o que precisa ser feito, sem ambiguidades. Isso inclui o mapeamento de dependências externas claras, como credenciais de homologação de gateways de pagamento externos (**RNF06**) ou diretrizes de retenção de arquivos no Google Cloud Storage (**RNF09**).

* **O requisito cabe em uma Sprint?**
  O requisito deve ser suficientemente pequeno para ser concluído dentro de uma única Sprint, respeitando a divisão atômica das funcionalidades de visualização e consumo do app (**RF01** a **RF10**) e de escrita/gestão no painel administrativo (**RF11** a **RF22**).

* **O requisito está representado por uma história de usuário?**
  O requisito deve ser descrito no formato de história de usuário (*User Story*), facilitando o entendimento do valor real gerado para a organização (administradores) ou para o público geral (doadores e voluntários) pelo time de desenvolvimento.

* **O requisito está mapeado para uma interface (quando necessário)?**
  Se o requisito envolve elementos de interface com o usuário no aplicativo móvel em Flutter ou no painel administrativo em Streamlit (**RNF03**), os protótipos de alta fidelidade ou *wireframes* devem estar definidos. Para o módulo móvel, o desenho deve obrigatoriamente respeitar a estrutura de três abas inferiores (*Feed, Transparência e Colaboração*) e a seção superior fixa institucional (**RNF07**).

* **As definições de arquitetura e contratos de API estão claras?**
  Para tarefas de back-end (**Python/FastAPI**), os contratos dos endpoints e esquemas de dados (**MongoDB**) devem estar estabelecidos. Toda e qualquer requisição deve prever obrigatoriamente a passagem e validação do hash de 32 dígitos (*partition key*) para assegurar o isolamento lógico dentro da arquitetura multi-tenant (**RNF01**).

---

## 9.2 Definition of Done (DoD)

O DoD é um acordo que demonstra a qualidade do requisito produzido, indicando que “Done” comprova a satisfação de todos com o trabalho realizado. Se um requisito não atende ao “Done”, ele não deve ser liberado ou apresentado na Sprint Review. Alguns itens que devem ser verificados para determinar se um requisito está “Done” são:

* **Entrega um incremento do produto?**
  A funcionalidade desenvolvida deve agregar valor ao produto como um todo, resultando em uma versão funcional e utilizável nos módulos móvel (**RF01** a **RF10**) ou administrativo (**RF11** a **RF22**).

* **Contempla os critérios de aceite estabelecidos?**
  Todos os critérios de aceitação definidos na história de usuário foram integralmente atendidos e validados através de testes manuais ou automatizados.

* **Está documentado para uso?**
  A documentação técnica da funcionalidade está atualizada e disponível. Isto inclui a atualização do Swagger/OpenAPI do back-end, comentários pertinentes no código e o registro de quaisquer novas variáveis institucionais ou de tema que devam constar no arquivo JSON de customização (**RNF02**).

* **Está aderente aos padrões de codificação?**
  O código foi desenvolvido seguindo estritamente as diretrizes e padrões estabelecidos para a stack tecnológica do projeto: **Python/FastAPI** no back-end, **MongoDB** no banco de dados, **Flutter** no aplicativo mobile e **Streamlit** no painel administrativo (**RNF03**).

* **Mantém os índices de performance do produto?**
  A funcionalidade implementada consome recursos de maneira otimizada e não degrada a experiência do usuário ou os tempos de resposta das chamadas de API, garantindo conformidade com os requisitos de usabilidade e eficiência do sistema.

* **O desenvolvimento foi concluído integralmente?**
  A funcionalidade cumpre todas as suas regras de negócio associadas de ponta a ponta. Todas as ações de engajamento do usuário (confirmar presença em evento, inscrição em voluntariado, contacto com a organização) devem ocorrer estritamente dentro do aplicativo, utilizando formulários embutidos e integrados, sem redirecionamentos externos (**RNF11**). Além disso, postagens do tipo "Evento" devem renderizar adequadamente o componente acoplado de inscrição (**RNF10**).

* **O isolamento de dados e segurança foram validados?**
  Foi verificado exaustivamente que todas as transações, consultas e mutações de dados exigem e validam a chave de partição (hash de 32 dígitos), impedindo o vazamento de informações entre organizações na arquitetura multi-tenant (**RNF01**). As restrições rígidas de acesso entre o papel de "Administrador Geral" único e "Administradores da Organização" (**RNF04**) foram validadas e testadas.

* **A conformidade legal e imutabilidade financeira foram aplicadas?**
  Caso a funcionalidade envolva o processamento de doações via webhook (**RF10**, **RNF06**), o sistema garante a omissão automática de dados de identificação pessoal (como nome e CPF) antes da persistência em banco caso o usuário selecione a opção de anonimato (**RNF05**). Adicionalmente, os registros financeiros resultantes são armazenados de forma blindada em modelo WORM através da funcionalidade *Object Retention Lock* do Google Cloud Storage (GCS) para auditorias futuras (**RNF08**, **RNF09**).

* **Os testes foram executados e aprovados?**
  Testes unitários, de integração e de validação funcional foram executados com sucesso, obtendo a cobertura mínima estipulada pelo time e garantindo que nenhuma regressão foi introduzida no repositório.

* **A funcionalidade foi revisada pela equipe?**
  O código correspondente foi submetido como um *Pull Request* no **GitHub** (**RNF03**), revisado por pelo menos um par de desenvolvimento, aprovado e integrado com sucesso na branch estável do projeto.

* **A documentação e o feedback relevante foram incorporados?**
  O resultado final reflete perfeitamente os alinhamentos e ajustes técnicos identificados pelo time de desenvolvimento, pelo Product Owner e pelas partes interessadas da organização.
