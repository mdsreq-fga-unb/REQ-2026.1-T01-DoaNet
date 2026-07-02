# DoaNet 💙

O **DoaNet** é uma plataforma *white label* para organizações sem fins lucrativos, desenvolvida na disciplina de **Requisitos de Software (REQ — T1, 2026.1)** da Universidade de Brasília (FGA). O projeto foi construído em parceria com a ONG **MoveEduca** e tem como objetivo aproximar organizações sociais de seus apoiadores, centralizando comunicação, voluntariado, doações e prestação de contas em um único aplicativo.

## ✨ Funcionalidades

- **Feed** — publicações e eventos da organização, com busca por título e filtro por tipo
- **Colaboração** — oportunidades de voluntariado com inscrição integrada
- **Doações** — fluxo completo de doação via gateway de pagamento (Stripe), com direcionamento (instituição ou projeto), visibilidade pública/anônima e rastreabilidade imutável (WORM)
- **Transparência** — histórico público e auditável de doações e despesas da organização
- **Painel Administrativo** — gerenciamento de feed, voluntariado, financeiro, administradores e customização
- **White Label** — nome, logotipo e cores da organização configuráveis, refletindo em todo o aplicativo

## 🏗️ Arquitetura

| Módulo | Tecnologia | Descrição |
| :--- | :--- | :--- |
| [`backend/`](backend/) | FastAPI + MongoDB | API REST com autenticação JWT, integração Stripe e Google Cloud Storage |
| [`frontend/`](frontend/) | Flutter | Aplicativo mobile/web para os usuários e apoiadores |
| [`streamlit/`](streamlit/) | Streamlit | Painel administrativo da organização |

## 📚 Documentação

A documentação completa do projeto — visão de produto, engenharia de requisitos, planejamento das sprints, atas de reunião e evidências — está publicada em:

🔗 **[mdsreq-fga-unb.github.io/REQ-2026.1-T01-DoaNet](https://mdsreq-fga-unb.github.io/REQ-2026.1-T01-DoaNet/)**

## 👥 Integrantes

| <img src="https://avatars.githubusercontent.com/u/187406144?v=4" width="100"> | <img src="https://avatars.githubusercontent.com/u/213525219?v=4" width="100"> | <img src="https://avatars.githubusercontent.com/u/205638471?v=4" width="100"> | <img src="https://avatars.githubusercontent.com/u/194005420?v=4" width="100"> | <img src="https://avatars.githubusercontent.com/u/68859909?v=4" width="100"> |
| :---: | :---: | :---: | :---: | :---: |
| **Davi Ursulino** | **João Leles** | **Letícia Vitória** | **Pedro Augusto** | **Pedro Druck** |
| [@DaviUrsulino](https://github.com/DaviUrsulino) | [@joaoleless](https://github.com/joaoleless) | [@leticiavitoriagomes](https://github.com/leticiavitoriagomes) | [@pedrorfb](https://github.com/pedrorfb) | [@pedruck](https://github.com/pedruck) |
