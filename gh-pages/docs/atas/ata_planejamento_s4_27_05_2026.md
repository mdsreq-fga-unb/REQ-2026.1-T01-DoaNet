# Sprint Planning — Sprint 4

**Data:** 27/05/2026 (quarta-feira)
**Local:** Discord
**Responsável pela Ata:** Letícia Vitória

## Participantes

**Equipe:** Davi Ursulino, João Leles, Letícia Vitória, Pedro Augusto e Pedro Druck

### Ausentes

Nenhum.

## Objetivos da Reunião

1. Definir o escopo e as User Stories da Sprint 4 com base nos encaminhamentos da revisão da Sprint 3.
2. Planejar o desenvolvimento do módulo de voluntariado e a integração com o painel admin.
3. Aplicar os critérios INVEST nas histórias selecionadas para o ciclo final.

## Discussões e Decisões

### Definição do Escopo da Sprint 4

A equipe alinhou que a Sprint 4 — última sprint do projeto — teria foco em **colaboração com a organização** através do módulo de voluntariado. Os entregáveis acordados foram:

- **US04** — visualização de oportunidades de voluntariado
- **US08** — inscrição do usuário como voluntário
- **US20** — criação de oportunidade de voluntariado (admin)
- **US21** — exclusão de oportunidade de voluntariado (admin)
- **US22** — atualização de oportunidade de voluntariado (admin)
- Expansão do painel admin no Streamlit (login implementado na Sprint 3) com gerenciamento de feed e oportunidades de voluntariado
- Documentação final da entrega

### Aplicação dos Critérios INVEST

As cinco histórias selecionadas (US04, US08, US20, US21, US22) foram avaliadas conforme os critérios INVEST durante a reunião e consideradas prontas para o desenvolvimento.

### Distribuição de Responsabilidades

A equipe manteve a divisão por frentes que vinha funcionando bem desde a Sprint 3:

- **Back-end:** Pedro Augusto e Davi Ursulino ficaram responsáveis pelos endpoints de voluntariado (visualização, criação, edição e exclusão).
- **Front-end Flutter:** Pedro Druck ficou responsável pelas telas de visualização e inscrição em voluntariado.
- **Front-end Admin:** Letícia Vitória ficou responsável pelas telas administrativas de voluntariado.
- **Expansão Admin:** João Leles ficou responsável por expandir o painel Streamlit (que continha apenas login/acesso de admin ao final da Sprint 3) com as telas de gerenciamento do feed e das oportunidades de voluntariado.

### Ponto de Atenção

A equipe sinalizou preocupação com a complexidade do formulário de inscrição em voluntariado (US08), que envolve coleta de múltiplos dados do candidato. Ficou decidido que esse fluxo seria monitorado de perto ao longo da sprint e revisado na reunião de refinamento.

## Encaminhamentos e Responsabilidades

| Atividade | Responsável | Prazo |
| :--- | :--- | :--- |
| Implementação dos endpoints de voluntariado (back-end) | Pedro Augusto e Davi Ursulino | 09/06/2026 |
| Implementação das telas de visualização e inscrição (Flutter) | Pedro Druck | 09/06/2026 |
| Implementação das telas administrativas de voluntariado | Letícia Vitória | 09/06/2026 |
| Expansão do painel Streamlit com gerenciamento de feed e voluntariado | João Leles | 09/06/2026 |
| Acompanhamento próximo do formulário de inscrição (US08) | Pedro Druck e Letícia Vitória | 09/06/2026 |
| Reunião de refinamento do User Story Map na semana intermediária | Equipe | 02/06/2026 |
| Preparação da entrega final do projeto e da documentação | Equipe | 09/06/2026 |
