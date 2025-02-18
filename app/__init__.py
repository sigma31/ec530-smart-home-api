from flask import Flask
from app.error_handlers import register_error_handlers

def create_app():
    app = Flask(__name__)

    # Load configuration settings
    app.config.from_object("app.config.Config")

    # Register error handlers
    register_error
