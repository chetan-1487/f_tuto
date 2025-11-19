from flask import Flask
from app.routes.users import user_bp
from .config import Config
from app.extension import db, migrate

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(user_bp)

if __name__ == "__main__":
    app.debug=True
    app.run(debug=True)
