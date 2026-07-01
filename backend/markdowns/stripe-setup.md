# Setup do Stripe — Guia para Novos Membros

Siga este guia para configurar o Stripe localmente e conseguir testar o fluxo de doação do DoaNet.

---

## Pré-requisitos

- Backend rodando (`poetry run uvicorn main:app --reload --host 127.0.0.1 --port 8000`)
- Frontend rodando (`flutter run -d chrome --web-browser-flag "--disable-web-security"`)
- Conta criada em [stripe.com](https://stripe.com) (gratuita, não precisa de dados bancários para testar)

---

## Passo 1 — Instalar o Stripe CLI

### Windows (PowerShell)

```powershell
winget install Stripe.StripeCLI
```

Feche e abra o terminal após a instalação.

### Linux (Debian/Ubuntu)

```bash
curl -s https://packages.stripe.dev/api/security/keypair/stripe-cli-gpg/public | gpg --dearmor | sudo tee /usr/share/keyrings/stripe.gpg > /dev/null

echo "deb [signed-by=/usr/share/keyrings/stripe.gpg] https://packages.stripe.dev/stripe-cli-debian-local stable main" | sudo tee /etc/apt/sources.list.d/stripe.list

sudo apt update && sudo apt install stripe
```

### Linux (Fedora/RHEL)

```bash
sudo dnf install stripe
```

### Linux (via script direto — qualquer distro)

```bash
curl -fsSL https://stripe.com/downloads/linux/stripe_linux_amd64.tar.gz | tar -xz
sudo mv stripe /usr/local/bin/
```

Verifique a instalação:

```bash
stripe --version
```

---

## Passo 2 — Autenticar o CLI com sua conta Stripe

```bash
stripe login
```

Abre o browser automaticamente. Clique em **Allow access** para vincular o CLI à sua conta.

---

## Passo 3 — Obter a chave secreta da API

1. Acesse [dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
2. Certifique-se de estar em modo **Test** (toggle no canto superior direito)
3. Copie a **Secret key** — começa com `sk_test_...`

---

## Passo 4 — Iniciar o listener de webhooks

Com o backend rodando, execute em um terminal separado:

```bash
stripe listen --forward-to localhost:8000/doacoes/webhook
```

O CLI imprimirá na primeira linha:

```
> Ready! Your webhook signing secret is whsec_abc123...
```

Copie esse valor — ele muda a cada execução.

---

## Passo 5 — Preencher o arquivo `.env`

Abra `backend/.env` e preencha os campos do Stripe:

```env
STRIPE_SECRET_KEY=sk_test_SUA_CHAVE_AQUI
STRIPE_WEBHOOK_SECRET=whsec_GERADO_NO_PASSO_4
STRIPE_SUCCESS_URL=http://localhost:8000/doacoes/sucesso
STRIPE_CANCEL_URL=http://localhost:8000/doacoes/cancelado
```

### Windows — editar pelo terminal:

```powershell
notepad backend\.env
```

### Linux — editar pelo terminal:

```bash
nano backend/.env
# ou
vim backend/.env
```

Reinicie o backend após salvar o `.env`.

---

## Passo 6 — Testar o fluxo

1. Abra o app no browser
2. Vá em **Colaboração** e clique em **Fazer Doação**
3. Preencha o formulário (valor, visibilidade, direcionamento)
4. Clique em **Ir para pagamento** — o Stripe Checkout abrirá no browser
5. Use o cartão de teste abaixo:

| Campo | Valor |
|---|---|
| Número do cartão | `4242 4242 4242 4242` |
| Validade | Qualquer data futura (ex: `12/34`) |
| CVC | Qualquer 3 dígitos (ex: `123`) |
| Nome / CEP | Qualquer valor |

6. Clique em **Pagar**
7. O Stripe redirecionará para a página de sucesso
8. No terminal do `stripe listen` você verá o evento `checkout.session.completed`
9. No MongoDB, o documento na collection `doacoes` terá `"status": "pago"`

---

## Cartões de teste adicionais

| Número | Resultado |
|---|---|
| `4242 4242 4242 4242` | Pagamento aprovado |
| `4000 0000 0000 0002` | Cartão recusado |
| `4000 0025 0000 3155` | Requer autenticação 3D Secure |

---

## Comandos de referência rápida

### Windows

```powershell
# Autenticar
stripe login

# Iniciar listener
stripe listen --forward-to localhost:8000/doacoes/webhook

# Rodar backend
poetry run uvicorn main:app --reload --host 127.0.0.1 --port 8000

# Rodar frontend
flutter run -d chrome --web-browser-flag "--disable-web-security"
```

### Linux

```bash
# Autenticar
stripe login

# Iniciar listener
stripe listen --forward-to localhost:8000/doacoes/webhook

# Rodar backend
poetry run uvicorn main:app --reload --host 127.0.0.1 --port 8000

# Rodar frontend
flutter run -d chrome --web-browser-flag "--disable-web-security"
```

---

## Observações importantes

- A `STRIPE_WEBHOOK_SECRET` (`whsec_...`) **é gerada a cada vez** que você roda `stripe listen`. Se reiniciar o CLI, atualize o `.env` e reinicie o backend.
- Em modo `sk_test_`, nenhuma cobrança real é feita.
- O `stripe listen` precisa estar rodando **ao mesmo tempo** que o backend para os webhooks funcionarem localmente.
- Nunca commite o arquivo `.env` — ele está no `.gitignore`.
