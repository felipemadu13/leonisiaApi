
# Projeto Leonísia

Este é o backend do projeto, desenvolvido com **Django** e utilizando o **Django REST Framework** para expor APIs. O projeto está configurado para utilizar um banco de dados SQLite e suporta CORS para comunicação com o frontend.

---

## Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas:

- **Python**: Necessário para executar o código do backend. A versão recomendada é 3.10 ou superior.
- **pip**: Gerenciador de pacotes do Python para instalar as dependências.
- **Virtualenv** (opcional): Ferramenta para criar ambientes isolados no Python. Isso ajuda a evitar conflitos entre dependências de diferentes projetos.

---

## Dependências

### Lista de bibliotecas utilizadas:
- **Django 5.1.3**: O framework principal para desenvolvimento web.
- **Django REST Framework**: Facilita a criação de APIs RESTful.
- **django-cors-headers**: Habilita a comunicação entre diferentes domínios (frontend e backend).
- **SQLite**: Banco de dados padrão para desenvolvimento, leve e embutido.

As dependências estão especificadas no arquivo `requirements.txt` e podem ser instaladas automaticamente.

---

## Instalação

### Etapas para configurar o ambiente:

1. **Clone o repositório:**
   - Este comando baixa o código do repositório remoto para sua máquina.
   ```bash
   git clone https://github.com/felipemadu13/leonisiaApi
   cd leonisiaApi
   ```

2. **Crie um ambiente virtual:**
   - Um ambiente virtual isola as dependências do projeto.
   - Em sistemas Unix/Linux/MacOS:
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```
   - Em sistemas Windows:
     ```bash
     python -m venv venv
     venv\Scriptsctivate
     ```

3. **Instale as dependências:**
   - Este comando instala todas as bibliotecas especificadas no `requirements.txt`.
   ```bash
   pip install -r requirements.txt
   ```

4. **Realize as migrações do banco de dados:**
   - Migrações criam e atualizam as tabelas do banco de dados conforme definido nos modelos.
   ```bash
   python manage.py migrate
   ```

5. **Inicie o servidor de desenvolvimento:**
   - Com este comando, você inicia o servidor Django local para testar o projeto.
   ```bash
   python manage.py runserver
   ```

   - O servidor estará disponível em: [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Estrutura do Projeto

Descrição dos principais diretórios e arquivos do projeto:

- **`manage.py`**: Arquivo principal para gerenciar o projeto Django. Usado para rodar o servidor, criar migrações, entre outros.
- **`accounts/`**: Aplicativo personalizado de autenticação, com templates para login e registro de usuários.
- **`db.sqlite3`**: Banco de dados local usado para armazenar informações durante o desenvolvimento.
- **`requirements.txt`**: Lista de dependências necessárias para rodar o projeto.

---

## Configurações de API

### Integração com o frontend:
- O backend segue os padrões do Django REST Framework, com suporte a endpoints RESTful.
- **Endpoints disponíveis**: Consulte a documentação ou explore os endpoints manualmente utilizando ferramentas como Postman ou diretamente no navegador.

### Habilitação de CORS:
- Configurado com `django-cors-headers` para permitir requisições vindas do frontend.

---

## Contribuindo

### Como contribuir para o projeto:

1. **Crie uma branch para suas alterações:**
   - Crie uma branch separada para trabalhar em novas funcionalidades ou correções.
   ```bash
   git checkout -b minha-feature
   ```

2. **Faça o commit das alterações:**
   - Após realizar suas alterações, salve-as no repositório local.
   ```bash
   git commit -m "Descrição das alterações"
   ```

3. **Envie as alterações para o repositório remoto:**
   - Suba a branch para o repositório no GitHub para análise e integração.
   ```bash
   git push origin minha-feature
   ```

---

### Observação Final

- Para usar o backend corretamente, certifique-se de que o frontend esteja configurado e se comunique com este servidor. Consulte o README do frontend para mais informações sobre essa integração.

---