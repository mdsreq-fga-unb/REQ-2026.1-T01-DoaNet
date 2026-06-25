# Evidências — Sprint 6

---

## User Stories

<a id="us01"></a>
### US01 — Visualizar histórico financeiro

> Como usuário, quero visualizar o histórico de doações e despesas da organização, para acompanhar a transparência financeira de forma auditável.

**Critérios de Aceite:**

- O histórico exibe doações e despesas em ordem cronológica decrescente.
- Cada registro apresenta tipo (doação/despesa), valor, data e descrição.
- O histórico é acessível sem autenticação pelo usuário comum.
- Os registros são imutáveis após lançamento — não podem ser editados ou excluídos.

<a id="us03"></a>
### US03 — Visualizar descrição da ONG

> Como usuário, quero visualizar uma descrição institucional da organização, para entender seu propósito e áreas de atuação.

**Critérios de Aceite:**

- A tela exibe nome, missão e descrição da organização.
- As informações refletem os dados configurados pelo administrador.
- A página é acessível sem autenticação.

<a id="us05"></a>
### US05 — Contactar a organização

> Como usuário, quero contactar os administradores da organização de forma integrada, para tirar dúvidas ou buscar mais informações.

**Critérios de Aceite:**

- O usuário acessa um canal de contato direto com a organização a partir da tela de perfil.
- O canal redireciona corretamente para o meio configurado (ex: WhatsApp, e-mail).

<a id="us12"></a>
### US12 — Cadastrar administrador de organização

> Como Administrador Geral, quero cadastrar um novo administrador para uma organização, para provisionar seu acesso ao painel de gestão.

**Critérios de Aceite:**

- O administrador geral consegue cadastrar um novo admin informando nome, e-mail e organização vinculada.
- O novo administrador acessa o painel imediatamente com as credenciais criadas.
- O sistema impede o cadastro de dois administradores com o mesmo e-mail.

<a id="us13"></a>
### US13 — Remover administrador de organização

> Como Administrador Geral, quero remover um administrador de organização, para revogar seu acesso e controle sobre o painel.

**Critérios de Aceite:**

- O administrador geral consegue remover qualquer administrador de organização.
- O acesso do administrador removido é revogado imediatamente após a remoção.
- A remoção não afeta dados históricos criados pelo administrador removido.

<a id="us14"></a>
### US14 — Configurar dados institucionais

> Como administrador da organização, quero configurar os dados de customização, para manter a interface do aplicativo alinhada ao branding da ONG (White Label).

**Critérios de Aceite:**

- O administrador consegue configurar nome, logotipo e cores da organização.
- As alterações são refletidas na interface do aplicativo em tempo real.
- Apenas administradores autenticados conseguem alterar os dados institucionais.

---

## Engenharia de Requisitos

### Evidências do Processo de ER

#### Verificação de Requisitos — Critérios INVEST

| User Story | I | N | V | E | S | T |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **US01** — Visualizar histórico financeiro | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| **US03** — Visualizar descrição da ONG | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| **US05** — Contactar a organização | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| **US12** — Cadastrar administrador de organização | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| **US13** — Remover administrador de organização | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| **US14** — Configurar dados institucionais | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |

> **I** — Independente · **N** — Negociável · **V** — Valiosa · **E** — Estimável · **S** — Suficientemente pequena · **T** — Testável

> ⚠️ Sprint em andamento — verificação a ser concluída na revisão final.

#### Critérios de Aceite — Evidências de Cumprimento

- [US01 — Visualizar histórico financeiro](#us01): ⚠️ Sprint em andamento
- [US03 — Visualizar descrição da ONG](#us03): ⚠️ Sprint em andamento
- [US05 — Contactar a organização](#us05): ⚠️ Sprint em andamento
- [US12 — Cadastrar administrador de organização](#us12): ⚠️ Sprint em andamento
- [US13 — Remover administrador de organização](#us13): ⚠️ Sprint em andamento
- [US14 — Configurar dados institucionais](#us14): ⚠️ Sprint em andamento

---

## Engenharia de Software

_A preencher._
