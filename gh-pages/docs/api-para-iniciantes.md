# Guia de API (Django + Postgres)

Este documento explica, do zero, o que e uma API, o que ela faz, e todas as etapas que acontecem quando voce envia uma requisicao HTTP. Vamos usar exemplos simples de autenticacao (signup, login, test-token) em um backend Django com Django REST Framework (DRF) e banco Postgres, usando o padrao MVC para organizar o backend e um frontend separado em Flutter.

## 1) O que e uma API

API (Application Programming Interface) é um conjunto de regras que define como um programa conversa com outro. Em uma API web:

- O cliente (navegador, app mobile, Postman, REST Client) envia uma requisicao HTTP.
- O servidor (Django) recebe, processa e responde.
- A resposta normalmente retorna em formato JSON.

Em resumo: a API é a "porta" do servidor para o mundo externo, com regras claras de entrada e saida.

## 2) O que uma API faz

Uma API:

- Recebe dados (ex.: username e password)
- Valida os dados
- Executa regras de negocio
- Lê e grava no banco de dados
- "Volta" e devolve uma resposta padronizada (status HTTP + JSON)

## 3) Componentes principais (MVC no backend)

No Django + DRF (backend) e Flutter (frontend):

- Model (M): representa os dados e as regras desses dados.
- Controller (C): recebe a requisicao e decide o que fazer (no Django, isso fica nas views).
- View (V): no MVC tradicional e a interface. Aqui essa parte fica no Flutter, nao no Django.
- Serializer: valida dados de entrada e transforma dados de saida em JSON.
- URL/Router: mapeia a rota para o controller.
- ORM: camada que conversa com o Postgres (sem escrever SQL direto).

Fluxo simplificado:

Flutter (cliente) -> URL -> Controller (view do Django) -> Serializer -> Model/ORM -> Banco -> Serializer -> Response

### 3.1) O que sao Models 

Model e a definicao do "formato" do que vai para o banco de dados. Pense nele como uma ficha que descreve:

- Qual e o nome da coisa (ex.: Usuario).
- Quais informacoes ela tem (ex.: username, email, password).
- Quais regras valem para esses dados (ex.: username nao pode repetir).

Quando voce define um Model, o Django cria a tabela no Postgres com as colunas correspondentes. Depois, voce pode criar, ler, atualizar e deletar registros sem escrever SQL.

Exemplo simples (ideia):

```python
class Usuario(models.Model):
  username = models.CharField(max_length=150, unique=True)
  email = models.EmailField()
```

Isso significa:

- Existe uma tabela de usuarios.
- Cada usuario tem username e email.
- O username e unico (nao pode repetir).

No seu projeto, o Model de usuarios ja existe (o Django tem o User pronto). Por isso o serializer usa esse Model para salvar os dados no Postgres.

## 4) Fases detalhadas de uma requisicao HTTP

A seguir esta o passo a passo do que acontece quando voce faz um POST ou GET.

### 4.1) Do cliente ate o servidor

1) Voce envia uma requisicao HTTP (ex.: POST /signup/).
2) Seu cliente resolve o dominio (ou usa 127.0.0.1).
3) O cliente abre uma conexao TCP com o servidor.
4) Se for HTTPS, ocorre o handshake TLS.
5) O cliente envia o cabecalho e o corpo da requisicao.

### 4.2) Dentro do Django

6) O servidor Django recebe a requisicao.
7) O URLConf (urls.py) encontra a rota correta (ex.: /signup/ -> signup view).
8) A View e chamada com os dados da requisicao.
9) A View cria o Serializer com request.data.
10) O Serializer valida os dados (is_valid()).
11) Se for valido, serializer.save() cria o usuario no banco.
12) A View pode gerar token de autenticacao.
13) A View retorna um Response com JSON e status HTTP.

### 4.3) Do servidor de volta ao cliente

14) O Django envia o JSON e o status (ex.: 201 Created).
15) O cliente recebe, interpreta e usa a resposta.

## 5) Exemplo real com as rotas de autenticacao

### 5.1) Signup (criar conta)

Requisicao:

```http
POST http://127.0.0.1:8000/signup/
Content-Type: application/json

{
  "username": "adam",
  "password": "Pass1234!",
  "email": "adam@mail.com"
}
```

O que acontece:

- URLConf envia para signup view.
- A view cria UserSerializer(data=request.data).
- O serializer valida os campos.
- serializer.save() grava o usuario no Postgres.
- Um token é criado para esse usuario.
- A resposta retorna o token e os dados do usuario.

Resposta esperada:

```json
{
  "token": "abc123...",
  "user": {
    "id": 1,
    "username": "adam",
    "email": "adam@mail.com"
  }
}
```

### 5.2) Login (entrar)

Requisicao:

```http
POST http://127.0.0.1:8000/login/
Content-Type: application/json

{
  "username": "adam",
  "password": "Pass1234!"
}
```

Fluxo esperado:

- A view valida username e password.
- Se correto, gera ou retorna o token.
- Responde com token e/ou dados do usuario.

## 6) O papel do Serializer

O serializer serve para:

- Validar campos (ex.: password, email)
- Converter entrada JSON em objeto Python (para se adequar ao modelo definido)
- Converter objeto Python em JSON de saida 

No seu projeto:

```python
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "email"]
```

Isso define exatamente quais campos que a API espera receber preenchido ao realizar uma requisição e quais campos ela devolve em caso de sucesso.

## 7) O papel do Postgres

- O Postgres armazena os dados de forma persistente.
- O Django usa o ORM para transformar Python em SQL.
- Quando voce chama serializer.save(), o ORM faz o INSERT, e insere os dados na database automaticamente.

## 8) Status HTTP mais comuns

- 200 OK: sucesso
- 201 Created: criado
- 400 Bad Request: dados invalidos
- 401 Unauthorized: token ausente ou invalido
- 404 Not Found: rota nao existe
- 500 Internal Server Error: erro no servidor

## 9) Checklist mental para debugar

Se algo nao funciona:

1) A rota existe no urls.py?
2) O metodo HTTP esta correto (GET/POST)?
3) Os campos enviados batem com o serializer?
4) O banco esta acessivel?
5) O token esta correto e no header certo?

## 10) Resumo final

- API e uma conversa padronizada entre cliente e servidor.
- Django recebe a requisicao, valida, salva no Postgres e responde JSON.
- Serializer define o que entra e o que sai.
- MVT organiza o projeto: Model (dados), View (logica), Template (interface). Em APIs, Template geralmente nao aparece.

Se quiser, posso complementar com um diagrama do fluxo ou ajustar o documento para o formato do seu mkdocs.
