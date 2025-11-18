from flask import Flask
from routes.users import user_bp
from .config import Config

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = Config.Database_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
app.secret_key = Config.Secret_key 

app.register_blueprint(user_bp, url_prefix="/users")

if __name__ == "__main__":
    app.debug=True
    app.run(debug=True)
