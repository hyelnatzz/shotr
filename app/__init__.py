from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()
login_manager = LoginManager()
admin = Admin()

def create_app(config):
    # create app instance
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth_bp.login'
    admin.init_app(app)

    #database models
    from .models import  Urls, User, ShortUrl
    
    #admin
    admin.add_view(ModelView(Urls, db.session))
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(ShortUrl, db.session))

    #blueprints
    from .auth import auth_bp
    from .urls import urls_bp
    from .user import user_bp
    from .views import home_bp

    #register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(urls_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(home_bp)

    with app.app_context():
        @login_manager.user_loader
        def loader(user_id):
            return User.query.get(int(user_id))
        db.create_all()
        return app

