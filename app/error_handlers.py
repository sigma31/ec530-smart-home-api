from flask import jsonify
from werkzeug.exceptions import HTTPException

def register_error_handlers(app):
    @app.errorhandler(HTTPException)
    def handle_exception(e):
        response = e.get_response()
        response.data = jsonify({
            "error": e.name,
            "code": e.code,
            "message": e.description
        }).data
        response.content_type = "application/json"
        return response
