import io
import uuid

from sqlalchemy_utils import UUIDType
from flask import current_app
from pyffmpeg import FFmpeg
import pydub

from app import db


class Base(db.Model):
    __abstract__ = True

    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())


class MusicFile(Base):
    id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    filename = db.Column(db.String)
    data = db.Column(db.LargeBinary)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", backref=db.backref("tracks", lazy=True))

    def __repr__(self) -> str:
        return f"Track {self.file_name}"

    def convert_wav_to_mp3(self) -> None:
        wav_song = io.BytesIO(self.data)
        mp3_song = io.BytesIO()
        pydub.AudioSegment.converter = FFmpeg().get_ffmpeg_bin()
        r = pydub.AudioSegment.from_file(wav_song, format="wav")
        r.export(mp3_song, format="mp3")
        self.data = mp3_song.read()
        self.filename = self.filename_without_extension() + ".mp3"

    def filename_without_extension(self) -> str:
        return self.filename.rsplit(".", 1)[0]

    def valid_extension(self) -> bool:
        return (
            "." in self.filename
            and self.filename.rsplit(".", 1)[1].lower()
            in current_app.config["MUSIC_ALLOWED_EXTENSIONS"]
        )


class User(Base):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    token = db.Column(UUIDType(binary=False), unique=True, default=uuid.uuid4)

    def __repr__(self) -> str:
        return f"User {self.name}"

    def validate_token(self, token: str) -> bool:
        return str(self.token) == token
