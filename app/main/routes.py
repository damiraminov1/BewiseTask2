import io

from flask import request, send_file

from app import db
from app.models import User, MusicFile
from app.main import bp


@bp.route(
    "/music/",
    methods=[
        "POST",
    ],
)
def upload_music():
    file = request.files.get("file")
    if not file or not file.filename:
        return {"message": "No file provided or incorrect filename."}, 400

    user_data: dict = request.form
    id: str = user_data.get("id")
    token: str = user_data.get("token")

    if not id or not token:
        return {"message": "No user id or token provided."}, 401

    user = db.session.query(User).filter(User.id == id).one_or_none()
    if not user or not user.validate_token(token=token):
        return {"message": "Not valid user id or token provided."}, 401

    music_file = MusicFile(filename=file.filename, data=file.read())
    if not music_file.valid_extension():
        return {"message": "Not valid file extension provided.."}

    music_file.convert_wav_to_mp3()
    music_file.user = user

    db.session.add(music_file)
    db.session.commit()
    return (
        f"{request.host_url}?record={music_file.id}&user_id={music_file.user_id}",
        201,
    )


@bp.route(
    "/",
    methods=["GET"],
)
def download_music():
    args: dict = request.args
    record_id: str = args.get("record")
    user_id: str = args.get("user_id")

    if not record_id or not user_id:
        return {"message": "No record id or user id provided."}, 401
    record = (
        db.session.query(MusicFile)
        .filter(MusicFile.id == record_id)
        .filter(MusicFile.user_id == user_id)
        .one_or_none()
    )

    if not record:
        return {"message": "Not valid record id or user id provided."}, 401
    return (
        send_file(
            io.BytesIO(record.data),
            mimetype="audio/mpeg3",
            download_name=record.filename,
            as_attachment=True,
        ),
        200,
    )
