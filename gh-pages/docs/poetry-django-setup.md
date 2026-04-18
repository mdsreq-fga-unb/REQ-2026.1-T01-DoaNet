# Guia de Onboarding do Backend: Poetry + Django + PostgreSQL em Docker

Este documento explica como rodar o backend a partir do estado atual do repositorio, sem criar projeto novo.

## Objetivo

- Instalar tudo que o backend atual precisa.
- Subir PostgreSQL via Docker.
- Conectar no banco pelo pgAdmin instalado na maquina.
- Aplicar migracoes e executar a API localmente.

## Estado atual do repositorio

- O backend ja existe na pasta `backend/`.
- O projeto usa Poetry com `pyproject.toml` e `poetry.lock`.
- O projeto ja usa Django, DRF e psycopg.
- O arquivo principal da aplicacao e `backend/manage.py`.

## 1. Pre-requisitos

- Python 3.13+ (o projeto exige `>=3.13`).
- Git.
- Poetry.
- Docker Desktop (com Docker Compose).
- pgAdmin instalado na maquina (Desktop).

Verifique:

```bash
python --version
git --version
poetry --version
docker --version
docker compose version
```

## 2. Clonar e entrar no backend

```bash
git clone <url-do-repositorio>
cd REQ-2026.1-T01-DoaNet/backend
```

## 3. Instalar dependencias Python do projeto

Recomendado para padronizar o ambiente virtual dentro da pasta do backend:

```bash
poetry config virtualenvs.in-project true
```

Instalar dependencias ja travadas no lockfile:

```bash
poetry install
```

## 4. Criar/validar arquivo .env do backend

No arquivo `backend/.env`, use:

```env
DB_NAME=<nome_do_banco>
DB_USER=<usuario_do_banco>
DB_PASSWORD=<senha_do_banco>
DB_HOST=localhost
DB_PORT=5431
```

Observacao:

- Com Django rodando na maquina host e Postgres no Docker, o host e `localhost` e a porta e a publicada no compose (`5431`).

## 5. Criar docker-compose.yml para PostgreSQL

Crie `backend/docker-compose.yml` com:

```yaml
services:
  postgres:
    image: postgres:16
    container_name: app_postgres
    restart: unless-stopped
    environment:
      POSTGRES_DB: [dado a ser preenchido]
      POSTGRES_USER: [dado a ser preenchido]
      POSTGRES_PASSWORD: [dado a ser preenchido]
    ports:
      - "5431:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U <usuario_do_banco> -d <nome_do_banco>"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  postgres_data:
```

Suba o banco:

```bash
docker compose up -d
docker compose ps
```

## 6. Conectar no PostgreSQL via pgAdmin Desktop

No pgAdmin instalado na maquina:

1. Abra o pgAdmin.
2. Clique em Add New Server.
3. Em General, defina Name: `DoaNet Local`.
4. Em Connection, use:
   - Host name/address: `[dado a ser preenchido]`
   - Port: `[dado a ser preenchido]`
   - Maintenance database: `[dado a ser preenchido]`
   - Username: `[dado a ser preenchido]`
   - Password: `[dado a ser preenchido]`
5. Salve.

## 7. Validar backend e aplicar migracoes

```bash
poetry run python manage.py check
poetry run python manage.py migrate
```

Se quiser criar superusuario:

```bash
poetry run python manage.py createsuperuser
```

## 8. Subir servidor Django

```bash
poetry run python manage.py runserver
```

Acesse: `http://127.0.0.1:8000`

## 9. Comandos diarios uteis

- Subir banco: `docker compose up -d`
- Parar banco: `docker compose down`
- Ver logs do banco: `docker compose logs -f postgres`
- Rodar comandos Django: `poetry run python manage.py <comando>`

## 10. O que versionar no Git

Manter versionado:

- `backend/pyproject.toml`
- `backend/poetry.lock`
- migracoes Django das apps

Nao versionar:

- `backend/.env`
- `backend/.venv/`

## 11. Solucao de problemas

### Erro de autenticacao no Postgres

- Verifique se `DB_USER` e `DB_PASSWORD` no `backend/.env` batem com `POSTGRES_USER` e `POSTGRES_PASSWORD` do compose.
- Se mudou credencial depois de criar volume, recrie os containers e o volume:

```bash
docker compose down -v
docker compose up -d
```

### Porta 5431 ocupada

- Troque o mapeamento de porta no compose (exemplo: `5433:5432`).
- Atualize `DB_PORT` no `backend/.env` com a mesma porta.

### Poetry usando Python errado

Use um Python 3.13 explicitamente:

```bash
poetry env use 3.13
poetry install
```

## Referencias

- Poetry: https://python-poetry.org/docs/
- Django: https://docs.djangoproject.com/
- DRF: https://www.django-rest-framework.org/
- Docker: https://docs.docker.com/
- pgAdmin: https://www.pgadmin.org/docs/
