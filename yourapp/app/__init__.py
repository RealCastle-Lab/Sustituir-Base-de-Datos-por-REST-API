from flask import Flask
from .routes import configure_routes
from .services import APIService

def create_app():
    app = Flask(__name__)
    # Configura la base URL de la API REST aquí
    api_service = APIService(base_url="http://api.example.com")

    configure_routes(app, api_service)
    return app
