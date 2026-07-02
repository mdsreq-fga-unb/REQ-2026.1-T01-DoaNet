
# 8 - DoR e DoD

## 8.1 Definition of Ready (DoR)

O DoR é um acordo entre o time e o Product Owner (PO) indicando quando um requisito estará preparado para ser puxado para uma Sprint. Alguns itens que podem ser verificados para determinar se um requisito está 'Ready' são:

* **O requisito possui informação necessária para ser trabalhado?**
  O requisito deve ter detalhes suficientes para que o time de desenvolvimento entenda o que precisa ser feito, sem ambiguidades. Isso inclui a identificação de dependências externas, acessos, credenciais, integrações ou informações necessárias para o desenvolvimento da funcionalidade.

* **O requisito cabe em uma Sprint?**
  O requisito deve ser suficientemente pequeno para ser concluído dentro de uma única Sprint, respeitando a divisão atômica das funcionalidades. Caso sua complexidade exceda a capacidade da equipe para o período planejado, ele deverá ser refinado e dividido em itens menores.

* **Os critérios de aceitação estão definidos?**
  A User Story deve possuir critérios de aceitação claros, objetivos e verificáveis, permitindo que a equipe compreenda as condições necessárias para considerar a funcionalidade concluída. Esses critérios devem servir como referência para o desenvolvimento, os testes e a validação da entrega.

* **O requisito está representado por uma história de usuário?**
  O requisito deve ser descrito no formato de história de usuário (*User Story*), facilitando o entendimento do valor real gerado para a organização, para o público geral e pelo time de desenvolvimento.

* **As definições de arquitetura e contratos de API estão claras?**
  Para funcionalidades que envolvam desenvolvimento de back-end, integrações ou persistência de dados, os contratos de API, esquemas de dados, restrições arquiteturais e demais decisões técnicas relevantes devem estar previamente definidos, de modo a orientar a implementação de forma consistente.

---

## 8.2 Definition of Done (DoD)

O DoD é um acordo que demonstra a qualidade do requisito produzido, indicando que “Done” comprova a satisfação de todos com o trabalho realizado. Se um requisito não atende ao “Done”, ele não deve ser liberado ou apresentado na Sprint Review. Alguns itens que devem ser verificados para determinar se um requisito está “Done” são:

* **Entrega um incremento do produto?**
  A funcionalidade desenvolvida deve agregar valor ao produto como um todo, resultando em uma versão funcional e utilizável nos módulos móvel ou administrativo.

* **Contempla os critérios de aceite estabelecidos?**
  Todos os critérios de aceitação definidos na história de usuário foram integralmente atendidos e validados através de testes manuais ou automatizados.

* **O desenvolvimento foi concluído integralmente?**
  A funcionalidade implementada atende às regras de negócio aplicáveis à respectiva história de usuário, contemplando todos os fluxos previstos e sem dependências pendentes.

* **Os testes foram executados e aprovados?**
  Testes unitários, de integração e de validação funcional foram executados com sucesso, obtendo a cobertura mínima de 70% e garantindo que nenhuma regressão foi introduzida no repositório.

* **A funcionalidade foi revisada pela equipe?**
  O código correspondente foi submetido como um *Pull Request* no **GitHub** (**RNF03**), revisado por pelo menos um par de desenvolvimento, aprovado e integrado com sucesso na branch estável do projeto.

* **A documentação e o feedback relevante foram incorporados?**
  O resultado final reflete perfeitamente os alinhamentos e ajustes técnicos identificados pelo time de desenvolvimento, pelo Product Owner e pelas partes interessadas da organização.


