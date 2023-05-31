import json

from flask import request

from app import db
from app.models import User
from app.auth import bp


@bp.route(
    "/register/",
    methods=[
        "POST",
    ],
)
def register():
    user_data: dict = json.loads(request.data.decode("utf-8"))
    username: str = user_data.get("username")
    if not username:
        return {"message": "No username provided."}, 400
    user = User(
        name=username,
    )
    db.session.add(user)
    db.session.commit()
    return {"id": user.id, "token": user.token}, 200
