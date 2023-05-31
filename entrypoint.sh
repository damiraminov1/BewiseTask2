poetry run flask db upgrade
exec poetry run gunicorn -w 4 --bind 0.0.0.0:5000 flask_app:app