# Sprint Planning — Sprint 5

**Data:** 09/06/2026 (terça-feira)
**Local:** Discord
**Responsável pela Ata:** Pedro Druck

## Participantes

**Equipe:** Davi Ursulino, João Leles, Letícia Vitória, Pedro Augusto e Pedro Druck

### Ausentes

Nenhum.

## Objetivos da Reunião

1. Definir o escopo e as User Stories da Sprint 5 com base nos encaminhamentos da revisão da Sprint 4.
2. Planejar o desenvolvimento do fluxo de doações no aplicativo e o início do registro no painel de transparência.
3. Incorporar o débito técnico herdado da Sprint 4 (formulário de inscrição em voluntariado — US08) ao planejamento.

## Discussões e Decisões

### Definição do Escopo da Sprint 5

A equipe alinhou que a Sprint 5 teria foco em **doações e rastreabilidade**, iniciando o registro no painel de transparência. Os entregáveis acordados foram:

- **US06** — filtrar o feed por tipo de publicação (normal/evento)
- **US07** — buscar publicação no feed por título
- **US10** — realização de doação no aplicativo, com direcionamento e visibilidade (pública/anônima)
- **US15** — lançamento manual de doações externas pelo administrador
- **US16** — lançamento de despesas operacionais pelo administrador
- Conclusão do débito técnico do formulário de inscrição em voluntariado (US08), conforme priorizado na retrospectiva da Sprint 4

### Integração com Gateway de Pagamento

Ficou decidido o uso do **Stripe** como gateway de pagamento para o fluxo de doações, com processamento criptografado e registro imutável após a confirmação (rastreabilidade via armazenamento WORM). A equipe destacou que esse é o ponto de maior risco técnico da sprint, por envolver integração externa.

### Aplicação dos Critérios INVEST

As histórias selecionadas (US06, US07, US10, US15, US16) foram avaliadas conforme os critérios INVEST durante a reunião e consideradas prontas para o desenvolvimento.

### Distribuição de Responsabilidades

- **Fluxo de doações (back-end + Stripe):** Pedro Augusto e Davi Ursulino
- **Fluxo de doações (front-end Flutter):** Pedro Druck
- **Lançamentos de doações externas e despesas (painel Streamlit):** Letícia Vitória
- **Filtro e busca no feed (Flutter):** João Leles
- **Débito técnico do formulário de voluntariado (US08):** Pedro Druck e Letícia Vitória

## Encaminhamentos e Responsabilidades

| Atividade | Responsável | Prazo |
| :--- | :--- | :--- |
| Implementação do fluxo de doações com Stripe (back-end) | Pedro Augusto e Davi Ursulino | 23/06/2026 |
| Implementação do formulário e fluxo de doação (Flutter) | Pedro Druck | 23/06/2026 |
| Telas de lançamento de doações externas e despesas (Streamlit) | Letícia Vitória | 23/06/2026 |
| Filtro por tipo e busca por título no feed (Flutter) | João Leles | 23/06/2026 |
| Conclusão do débito técnico do formulário de voluntariado (US08) | Pedro Druck e Letícia Vitória | 16/06/2026 |
| Reunião de refinamento do User Story Map na semana intermediária | Equipe | 16/06/2026 |
