from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Error Handling using the Werkzeug WSGI library
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

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(debug=True)
