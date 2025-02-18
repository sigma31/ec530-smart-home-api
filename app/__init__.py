from flask import Flask
from app.error_handlers import register_error_handlers

def create_app():
    app = Flask(__name__)
    
    # Register error handlers
    register_error_handlers(app)

    return app

