# Refinamento do User Story Map — Sprint 5

**Data:** 16/06/2026  
**Local:** Discord  
**Participantes:** Davi Ursulino, João Leles, Letícia Vitória, Pedro Augusto e Pedro Druck

## Pauta

- Revisão do progresso das histórias da sprint (US06, US07, US10, US15, US16)
- Refinamento do User Story Map com foco no fluxo de doações e nos registros de transparência
- Verificação da conclusão do débito técnico do formulário de voluntariado (US08)
- Alinhamento sobre a integração com o Stripe e o armazenamento imutável (WORM) dos comprovantes de doação

## Discussões

- O débito técnico do formulário de inscrição em voluntariado (US08) foi dado como **concluído**, encerrando a pendência da Sprint 4.
- O back-end do fluxo de doações está com o checkout do Stripe funcional; o front-end Flutter precisou de ajustes extras no formulário de doação (validações de CPF/endereço), consumindo mais tempo do que o previsto.
- O filtro (US06) e a busca (US07) do feed estão implementados e em fase de testes.
- Os lançamentos manuais do painel admin (US15, US16) estão funcionais, com confirmação em duas etapas para garantir a imutabilidade dos registros.
- A equipe alinhou o escopo do que entra no documento de requisitos da entrega da Unidade 3 (16/06), destacando as funcionalidades ligadas ao fluxo de doação e transparência.

## Encaminhamentos

| Atividade | Responsável | Prazo |
| :--- | :--- | :--- |
| Conclusão dos ajustes do formulário de doação no Flutter | Pedro Druck | 23/06/2026 |
| Registro das doações confirmadas no painel de transparência (webhook Stripe) | Pedro Augusto e Davi Ursulino | 23/06/2026 |
| Testes integrados do fluxo completo de doação (app → Stripe → transparência) | Equipe | 23/06/2026 |
| Testes finais de filtro e busca no feed | João Leles | 23/06/2026 |
| Preparação da apresentação do incremento para validação com o cliente | Davi Ursulino | 23/06/2026 |
