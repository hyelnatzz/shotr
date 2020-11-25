from flask import Flask
import os

def create_app():
    # create app instance
    app = Flask(__name__)
    app.secret_key = os.urandom(8).hex()

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

