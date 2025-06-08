from flask import Blueprint, request, jsonify, current_app
import jwt
from functools import wraps
from Player import Player, db
import uuid
import datetime

auth_bp = Blueprint("/auth", __name__)


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        if not token:
            return jsonify({"message": "Token is missing!"}), 401
        try:
            data = jwt.decode(
                token, current_app.config["SECRET_KEY"], algorithms=["HS256"]
            )
            current_user = data["username"]
        except Exception as e:
            return jsonify({"message": "Token is invalid!"}), 401
        return f(current_user, *args, **kwargs)

    return decorated


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    user = Player.query.filter_by(UserUserName=username, UserPassWord=password).first()

    if user:
        token = jwt.encode(
            {
                "userID": user.UserID,
                "username": user.UserUserName,
                "exp": int(
                    (datetime.datetime.now() + datetime.timedelta(days=30)).timestamp()
                ),
            },
            current_app.config["SECRET_KEY"],
            algorithm="HS256",
        )
        return jsonify({"token": token}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("userName")
    password = data.get("passWord")
    fullname = data.get("fullName", "")
    phone = data.get("phone", "")
    email = data.get("email", "")
    elo = data.get("elo", 1200)
    user_id = str(uuid.uuid4())[:10]

    # Kiểm tra username đã tồn tại chưa
    if Player.query.filter_by(UserUserName=username).first():
        return jsonify({"message": "Username already exists"}), 400

    # Tạo user mới
    new_user = Player(
        UserID=user_id,
        UserName=username,
        UserFullName=fullname,
        UserPhone=phone,
        UserEmail=email,
        UserElo=elo,
        UserUserName=username,
        UserPassWord=password,
        UserStatus="offline",
    )
    try:
        from api import db

        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"message": "Registration failed", "error": str(e)}), 500


@auth_bp.route("/logout", methods=["POST"])
@token_required
def logout(current_user):
    return jsonify({"message": f"{current_user} logged out successfully"}), 200
