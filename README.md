# Bewise Task 2

## Docker Deploy

### 1. Create .env file with variables below:
```dotenv
SECRET_KEY="you-will-never-guess"
POSTGRES_USER=postgres
POSTGRES_PASSWORD=passwordpostgresql
POSTGRES_DB=bewise_db_2
POSTGRES_HOSTNAME=postgres
```
### 2. Deploy:
```shell
docker-compose up -d
```


## Development [![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-311/)

### 1. Install [PostgreSQL](https://www.postgresql.org/)

### 2. Install [Poetry](https://python-poetry.org)

### 3. Install dependencies:
```shell
poetry install --with dev
```
### 4. Create .env file with variables below:
```dotenv
SECRET_KEY=generate-random-symbols
POSTGRES_USER=paste-here-postgres-username
POSTGRES_PASSWORD=paste-here-postgres-password
POSTGRES_DB=bewise_db_2
POSTGRES_HOSTNAME=localhost
```
### 5. Change .flaskenv with variables below:
```dotenv
FLASK_ENV=development
FLASK_DEBUG=1
```
### 6. Migrations:
```shell
poetry run flask db upgrade
```
### 7. Run:
```shell
poetry run flask run
```

## Usage
### 1. Create user:
```shell
curl --location 'http://127.0.0.1:5000/register/' \
--header 'Content-Type: text/plain' \
--data '{
    "username": "damir"
}'
```
### Answer:
```json
{
    "id": 1,
    "token": "b8bcbe26-a873-42d8-be3c-c9112ba213d3"
}
```
### 2. Send audio recording in wav format to server:

### 2.1 Offline (Basic logic)
```shell
curl --location 'http://127.0.0.1:5000/music/' \
--form 'id="1"' \
--form 'token="b8bcbe26-a873-42d8-be3c-c9112ba213d3"' \
--form 'file=@"/C:/Users/damir/Desktop/sample3.wav"'
```

### 2.2 Online (Easy to try)
```shell
curl -O https://filesamples.com/samples/audio/wav/sample3.wav &&
curl --location 'http://127.0.0.1:5000/music/' \
--form 'id="1"' \
--form 'token="b8bcbe26-a873-42d8-be3c-c9112ba213d3"' \
--form 'file=@sample3.wav'
```

### Answer:
```
http://127.0.0.1:5000/?record=43ed9a77-684b-4579-98fe-3959d96ed0be&user_id=1
```
### 3. Follow this link and download mp3 file from any browser:
```
http://127.0.0.1:5000/?record=43ed9a77-684b-4579-98fe-3959d96ed0be&user_id=1
```
