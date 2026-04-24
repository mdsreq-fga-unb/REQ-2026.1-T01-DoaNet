# Setup do Backend (Poetry + Django + Postgres)

Este guia mostra como preparar o ambiente do zero, usando o Poetry para criar o ambiente virtual e executar comandos basicos do Django. O projeto e um backend Django + DRF com Postgres.

## 1) Pre-requisitos

- Python 3.13+
- Git
- Docker Desktop (ou Docker Engine)
- Poetry

Verifique se esta tudo instalado:

```bash
python --version
git --version
docker --version
poetry --version
```

## 2) Instalar o Poetry com pip/pipx

### Passo 1: garantir pipx

No Windows (PowerShell):

```powershell
py -m pip install --user pipx
py -m pipx ensurepath
```

No Linux (bash):

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

Feche e abra o terminal e confirme:

```powershell
pipx --version
```

Se o comando nao aparecer, adicione o caminho do pipx ao PATH:

```
%USERPROFILE%\.local\bin
%APPDATA%\Python\Scripts
```

No Linux, o caminho comum e:

```
~/.local/bin
```

### Passo 2: instalar o Poetry via pipx

```powershell
pipx install poetry
```

No Linux (bash):

```bash
pipx install poetry
```

Confirme:

```powershell
poetry --version
```

### Alternativa: instalar via pip (menos recomendado)

```powershell
py -m pip install --user poetry
```

No Linux (bash):

```bash
python3 -m pip install --user poetry
```

Depois confirme com:

```powershell
poetry --version
```

## 3) Clonar o repositorio e entrar no backend

```bash
git clone <url-do-repositorio>
cd REQ-2026.1-T01-DoaNet/backend
```

## 4) Configurar o ambiente virtual do Poetry

Crie o venv dentro da pasta do projeto:

```bash
poetry config virtualenvs.in-project true
```

Instale as dependencias do projeto:

```bash
poetry install
```

Para abrir o shell do ambiente:

```bash
poetry shell
```

Ou rode comandos direto com:

```bash
poetry run <comando>
```

## 5) Preencher o .env (sem dados sensiveis)

Crie `backend/.env` com este formato:

```env
DB_NAME=<nome_do_banco>
DB_USER=<usuario_do_banco>
DB_PASSWORD=<senha_do_banco>
DB_HOST=localhost
DB_PORT=5431
SECRET_KEY=<sua_secret_key>
```

Como gerar a SECRET_KEY:

```bash
poetry run python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copie o valor gerado para o `SECRET_KEY`.

## 6) Subir o Postgres com Docker (sem compose)

Defina primeiro os valores que voce vai usar. Eles precisam ser os mesmos do `.env`:

- DB_NAME -> nome do banco
- DB_USER -> usuario do banco
- DB_PASSWORD -> senha do banco
- DB_PORT -> porta exposta (ex.: 5431)

Depois, rode o container:

```bash
docker run -d \
	--name app_postgres \
	-e POSTGRES_DB=<nome_do_banco> \
	-e POSTGRES_USER=<usuario_do_banco> \
	-e POSTGRES_PASSWORD=<senha_do_banco> \
	-p 5431:5432 \
	-v postgres_data:/var/lib/postgresql/data \
	postgres:16
```

Relacao com o `.env` (exemplo):

```env
DB_NAME=<nome_do_banco>
DB_USER=<usuario_do_banco>
DB_PASSWORD=<senha_do_banco>
DB_HOST=localhost
DB_PORT=5431
```

Para validar se o container esta rodando:

```bash
docker ps
```

Para parar e remover:

```bash
docker stop app_postgres
docker rm app_postgres
```

Aviso de seguranca: nao coloque senhas reais nem `SECRET_KEY` em arquivos versionados. Guarde segredos apenas no `.env` (que fica no `.gitignore`).

## 7) Comandos basicos do Django (com explicacao)

Todos os comandos devem ser rodados com `poetry run` para usar o ambiente do projeto.

### Verificar o projeto

```bash
poetry run python manage.py check
```

- Faz uma validacao geral das configuracoes.

### Criar migracoes

```bash
poetry run python manage.py makemigrations
```

- Cria arquivos de migracao quando voce altera Models.

### Aplicar migracoes

```bash
poetry run python manage.py migrate
```

- Aplica as migracoes no banco (cria tabelas e altera schemas).

### Criar superusuario

```bash
poetry run python manage.py createsuperuser
```

- Cria um usuario admin para acessar a area administrativa.

### Rodar o servidor local

```bash
poetry run python manage.py runserver
```

- Sobe o servidor em `http://127.0.0.1:8000`.

## 8) Fluxo tipico para iniciar o projeto

1. `poetry install`
2. Preencher o `backend/.env`
3. `docker run ...` (ver secao 6)
4. `poetry run python manage.py migrate`
5. `poetry run python manage.py runserver`

## 9) O que versionar no Git

Manter versionado:

- `backend/pyproject.toml`
- `backend/poetry.lock`
- Codigo do Django
- Migracoes das apps

Nao versionar:

- `backend/.env`
- `backend/.venv/`

## 10) Solucao de problemas comuns

### Erro de autenticacao no Postgres

- Confirme que `DB_USER` e `DB_PASSWORD` no `.env` batem com o `docker run`.
- Se voce mudou credenciais depois do container criado:

```bash
docker stop app_postgres
docker rm app_postgres
docker volume rm postgres_data
```

Depois rode novamente o comando do `docker run` com os novos valores.

### Porta 5431 ocupada

- Troque o mapeamento no `docker run`, por exemplo `-p 5433:5432`.
- Atualize `DB_PORT` no `.env`.

### Poetry usando Python errado

```bash
poetry env use 3.13
poetry install
```

## Referencias

- Poetry: https://python-poetry.org/docs/
- Django: https://docs.djangoproject.com/
- DRF: https://www.django-rest-framework.org/
- Docker: https://docs.docker.com/
