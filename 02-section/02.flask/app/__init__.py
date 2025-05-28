from flask import Flask
from .config import Config

from .usuarios.usuario_controller import usuario_controller
# from .prediccion.routes import routes_prediccion

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # eventos_routes = EventosRoutes(app)
    app.register_blueprint(usuario_controller)
    # app.register_blueprint(routes_prediccion)

    return app