from flask import Flask, jsonify
from flask_cors import CORS
from auth import auth_bp
from room import room_bp
from game import game_bp
from Player import db

app = Flask(__name__)
CORS(app)
app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:duchungpro108@localhost/chinese_chess"
)
db.init_app(app)

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(room_bp, url_prefix="/rooms")
app.register_blueprint(game_bp, url_prefix="/games")

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Hello, world!"}), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
