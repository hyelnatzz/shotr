from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config):
    # create app instance
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)



    #import blueprints
    from .auth import auth_bp
    from .urls import urls_bp
    from .user import user_bp
    from .views import home_bp

    #register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(urls_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(home_bp)


    return app

