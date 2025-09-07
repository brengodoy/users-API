from flask import Flask, jsonify
from interfaces.user_routes import user_bp
from domain.exceptions import CustomError
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
    JWTManager(app)
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