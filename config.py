import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{os.environ.get('POSTGRES_USER')}:"
        f"{os.environ.get('POSTGRES_PASSWORD')}"
        f"@{os.environ.get('POSTGRES_HOSTNAME')}:5432/{os.environ.get('POSTGRES_DB')}"
    )
    MUSIC_ALLOWED_EXTENSIONS = frozenset(
        [
            "wav",
        ]
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
