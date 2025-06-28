from flask import Flask
from flask_bcrypt import Bcrypt
from flask_limiter import Limiter
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_limiter.util import get_remote_address

from src.config import Config
from src.firewall import Firewall


db = SQLAlchemy()
bcrypt = Bcrypt()
firewall = Firewall()
limiter = Limiter(key_func=get_remote_address, default_limits=[])

login_manager = LoginManager()
login_manager.login_view = 'clients.login'
login_manager.login_message_category = 'info'

def create_app(config_class=Config):

    app = Flask(__name__, template_folder="templates")
    app.config.from_object(config_class)

    db.init_app(app=app)
    bcrypt.init_app(app=app)
    login_manager.init_app(app=app)
    firewall.init_app(app=app)
    limiter.init_app(app=app)

    from src.transactions.routes import transaction
    from src.clients.routes import clients
    from src.main.routes import main

    app.register_blueprint(transaction)
    app.register_blueprint(clients)
    app.register_blueprint(main)

    return app
