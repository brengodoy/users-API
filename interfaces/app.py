from flask import Flask, jsonify
from interfaces.user_routes import user_bp
from domain.exceptions import CustomError

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_bp)
    
    @app.errorhandler(CustomError)
    def handle_custom_error(error):
        response = jsonify({
			"error" : error.message
		})
        response.status_code = error.status_code
        return response
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)