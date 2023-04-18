from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'security'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Note
       
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app
'''
Flask-SQLAlchemy 3 no longer accepts an app argument to methods like create_all. Instead, it always requires an active Flask application context.
There is no need for that create_database function. SQLAlchemy will already not overwrite an existing file, and the only time the database wouldn't be created is if it raised an error.
'''
def create_database(app):
     if not path.exists('website/' + DB_NAME):
        with app.app_context(): #solucion al problerma anterior
            db.create_all()
            print('Created Database!')