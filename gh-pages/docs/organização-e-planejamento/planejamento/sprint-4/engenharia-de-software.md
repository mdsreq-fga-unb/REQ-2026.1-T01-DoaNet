# Sprint 4 — Engenharia de Software

[← Voltar ao Objetivo Geral](objetivo-geral.md)

## Descrição da Entrega

Implementação da parte de colaboração com a organização — registro de participação em voluntariados e administração do conteúdo entregue (feed e oportunidades) de forma centralizada no painel admin.

!!! warning "Observação"
    Na parte do voluntariado houve um **débito técnico**: o preenchimento do formulário da oportunidade de voluntariado não foi totalmente concluído.

## Definition of Ready — DoR

> Critérios verificados **antes** do início da sprint.

| Critério | Status | Evidência |
| :--- | :---: | :--- |
| O requisito possui informação necessária para ser trabalhado? | ✅ | US04, US08, US20, US21 e US22 detalhadas no Story Map com fluxos de CRUD e inscrição definidos |
| O requisito cabe em uma Sprint? | ✅ | 5 USs do módulo de voluntariado planejadas para 2 semanas; encaminhamentos na [Ata 5](../../../atas/ata5_26_05_2026.md) |
| Os critérios de aceitação estão definidos? | ✅ | US04, US08, US20, US21 e US22 formalizadas no Story Map |
| O requisito está representado por uma história de usuário? | ✅ | Requisitos representados por US04, US08, US20, US21 e US22 |
| As definições de arquitetura e contratos de API estão claras? | ✅ | Endpoints de voluntariado e painel admin definidos com base na arquitetura consolidada |

## Definition of Done — DoD

> Critérios verificados **ao final** da sprint.

| Critério | Status | Evidência |
| :--- | :---: | :--- |
| Entrega um incremento do produto? | ✅ | Módulo de voluntariado (CRUD e inscrição) e painel admin entregues e funcionais |
| Contempla os critérios de aceite estabelecidos? | ⚠️ | Cliente aprovou as entregas na [Ata 6](../../../atas/ata6_09_06_2026.md); débito técnico no formulário de inscrição |
| O desenvolvimento foi concluído integralmente? | ⚠️ | Fluxo de voluntariado funcional, porém formulário de inscrição incompleto (débito técnico registrado na [Ata 6](../../../atas/ata6_09_06_2026.md)) |
| Os testes foram executados e aprovados? | ⚠️ | Cobertura de testes incompleta, principalmente nas novas alterações do módulo de administrador |
| A funcionalidade foi revisada pela equipe? | ✅ | Revisão realizada nos Pull Requests #37 e #38 |
| A documentação e o feedback relevante foram incorporados? | ✅ | Débito técnico documentado; encaminhamentos para Sprint 5 definidos na [Ata 6](../../../atas/ata6_09_06_2026.md) |

<a id="débito-técnico"></a>

## Débito Técnico

> **US08 / Formulário de Voluntariado:** o preenchimento do formulário da oportunidade de voluntariado não foi inteiramente concluído na Sprint 4. O cliente aprovou o incremento na [Ata de Validação S4 (09/06/2026)](../../../atas/ata6_09_06_2026.md), mas o item foi **formalmente registrado como débito técnico** e **encaminhado para a Sprint 5**. Pendências associadas:
>
> - Conclusão do formulário de inscrição (nome, contato e motivação) com confirmação visual de envio.
> - Garantir que a inscrição fique visível para o administrador no painel Streamlit.
> - Cobertura de testes das alterações do módulo de voluntariado/administrador.

## Demonstração em Imagens

![Colab](../../../assets/Colab.png)

![Colab2](../../../assets/Colab2.png)