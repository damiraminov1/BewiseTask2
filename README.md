# Bewise Task 2

# Docker Deploy [![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-311/)

1. Create .env file with variables below:
```
SECRET_KEY="you-will-never-guess"
POSTGRES_USER=postgres
POSTGRES_PASSWORD=passwordpostgresql
POSTGRES_DB=bewise_db_1
POSTGRES_HOSTNAME=postgres
```
2. Deploy:
```
docker-compose up
```


# Development [![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-311/)

1. Install [PostgreSQL](https://www.postgresql.org/)

2. Install [Poetry](https://python-poetry.org)

3. Install dependencies:
```
poetry install --with dev
```
4. Create .env file with variables below:
```
SECRET_KEY=generate-random-symbols
POSTGRES_USER=paste-here-postgres-username
POSTGRES_PASSWORD=paste-here-postgres-password
POSTGRES_DB=bewise_db_1
POSTGRES_HOSTNAME=localhost
```
5. Change .flaskenv with variables below:
```
FLASK_ENV=development
FLASK_DEBUG=1
```
6. Migrations:
```
poetry run flask db upgrade
```
7. Run:
```
poetry run flask run
```