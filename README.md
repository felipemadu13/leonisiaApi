
# Projeto Backend - Django

Este é o backend do projeto, desenvolvido com **Django** e utilizando o **Django REST Framework** para expor APIs. O projeto está configurado para utilizar um banco de dados SQLite e suporta CORS para comunicação com o frontend.

## Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas:

- [Python](https://www.python.org/) (versão 3.10 ou superior)
- [pip](https://pip.pypa.io/en/stable/) (gerenciador de pacotes do Python)
- [Virtualenv](https://virtualenv.pypa.io/) (opcional, mas recomendado)

## Dependências

O projeto utiliza as seguintes bibliotecas:

- **Django 5.1.3**: Framework principal.
- **Django REST Framework**: Para criação de APIs.
- **django-cors-headers**: Para suporte a CORS.
- **SQLite**: Banco de dados padrão.

## Instalação

Siga as etapas abaixo para configurar o ambiente de desenvolvimento:

1. **Clone o repositório:**
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd back
   ```

2. **Crie um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Realize as migrações do banco de dados:**
   ```bash
   python manage.py migrate
   ```

5. **Inicie o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

O servidor estará disponível em [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Estrutura do Projeto

- **`manage.py`**: Arquivo de gerenciamento do projeto.
- **`accounts/`**: Aplicativo de autenticação com templates personalizados.
- **`db.sqlite3`**: Banco de dados local.
- **`requirements.txt`**: Dependências do projeto.

## Configurações de API

As APIs seguem os padrões do Django REST Framework. Você pode explorar as rotas disponíveis acessando o endpoint raiz ou integrando com o frontend. (Siga os passos do README.md do frontend)

## Contribuindo

1. Crie uma branch para suas alterações:
   ```bash
   git checkout -b minha-feature
   ```
2. Faça o commit das alterações:
   ```bash
   git commit -m "Descrição das alterações"
   ```
3. Envie as alterações:
   ```bash
   git push origin minha-feature
   ```

