from src.app import app

@app.errorhandler(400)
def bad_request(error):
    return {"error": "Bad Request: " + str(error)}, 400

@app.errorhandler(404)
def not_found(error):
    return {"error": "Not Found: " + str(error)}, 404

@app.errorhandler(500)
def internal_server_error(error):
    return {"error": "Internal Server Error: " + str(error)}, 500
