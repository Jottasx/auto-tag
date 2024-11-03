from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Cria a instância 
db = SQLAlchemy()

def create_app():
    # Criando e configurando a aplicação Flask
    app = Flask(__name__)
    app.config.from_object(Config)

    # Vincula o banco de dados com a aplicação
    db.init_app(app)

    with app.app_context():
        # Importa os modelos de banco e depois cria
        from app import models 
        db.create_all()

    # Carrega as rotas
    from app.routes import main
    app.register_blueprint(main)

    return app