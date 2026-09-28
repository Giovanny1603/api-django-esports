# API E-sports - 3ª Avaliação A2 (Django)

API RESTful desenvolvida em Django e Django REST Framework para gerenciamento de equipes e jogadores de E-sports.

## Como rodar o projeto localmente

1. Clone este repositório.

2. Crie e ative o ambiente virtual:
   `python -m venv venv`
   `.\venv\Scripts\activate`

3. Instale as dependências:
   `pip install -r requirements.txt`

4. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
   `DEBUG=True`
   `SECRET_KEY=sua-chave-secreta`
   `DATABASE_URL=sqlite:///db.sqlite3`

5. Execute as migrações para criar o banco de dados:
   `python manage.py migrate`
   
6. Inicie o servidor:
   `python manage.py runserver`