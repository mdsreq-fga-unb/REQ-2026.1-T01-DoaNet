# Retrospectiva — Sprint 5

**Data:** 23/06/2026  
**Local:** Discord  
**Responsável pela Ata:** Pedro Augusto

## Participantes

**Equipe:** Davi Ursulino, João Leles, Letícia Vitória, Pedro Augusto e Pedro Druck

### Ausentes

Nenhum.

## Objetivos da Reunião

1. Coletar as percepções individuais dos membros sobre o andamento da Sprint 5.
2. Avaliar a resolução do débito técnico herdado da Sprint 4.
3. Definir encaminhamentos para a sprint final do projeto.

## Discussões e Decisões

### Comentários dos Membros

**Davi Ursulino**
> O back-end conseguiu suprir as demandas do fluxo de doação sem grandes sustos, a integração com o Stripe foi mais tranquila do que esperávamos. O ponto de atenção foi o front-end, que precisou de ajustes extras que tomaram tempo da reta final.

**João Leles**
> O filtro e a busca do feed fluíram bem e deu para entregar com testes. Achei positivo termos formalizado o débito técnico da sprint passada em ata, isso fez ele ser atacado logo no início em vez de ficar se arrastando.

**Letícia Vitória**
> As telas de lançamento no painel admin ficaram prontas dentro do prazo e a confirmação em duas etapas evitou registros acidentais. A sprint foi mais equilibrada que a anterior em termos de organização pessoal da equipe.

**Pedro Augusto**
> A integração com o gateway de pagamento era o maior risco da sprint e foi mitigada cedo, o que deu folga para os testes integrados. O aprendizado da retrospectiva passada sobre débitos técnicos funcionou na prática.

**Pedro Druck**
> O formulário de doação no Flutter exigiu mais validações do que o previsto (CPF, endereço), o que gerou ajustes extras. Mesmo assim, o fluxo completo foi entregue e validado pelo cliente. Concluir o débito técnico do formulário de voluntariado logo na primeira semana foi a decisão certa.

### Principais Aprendizados

- Formalizar débitos técnicos em ata e priorizá-los no início da sprint seguinte funcionou: o formulário de voluntariado (US08) foi concluído sem comprometer as entregas novas.
- Integrações externas (gateway de pagamento) devem ser atacadas no início da sprint, por concentrarem o maior risco técnico — a antecipação evitou surpresas na reta final.
- Formulários com validação de dados pessoais tendem a consumir mais tempo de front-end do que o estimado; considerar esse custo nas próximas estimativas.

## Encaminhamentos e Responsabilidades

| Atividade | Responsável | Prazo |
| :--- | :--- | :--- |
| Incorporar o feedback do cliente (ícone nas caixas de voluntariado) ao planejamento da Sprint 6 | Toda a equipe | Sprint 6 |
| Manter a prática de formalizar débitos técnicos em ata | Toda a equipe | Sprint 6 |
| Planejar a Sprint 6 como sprint de fechamento (transparência, customização e admin) | Toda a equipe | 23/06/2026 |
