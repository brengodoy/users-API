from flask import request, jsonify, Blueprint
from infrastructure.user_repository import UserRepositorySQLite
from application.create_user import create_user
from application.login_user import login_user
from flask_jwt_extended import create_access_token

user_bp = Blueprint("users", __name__)

@user_bp.route("/users",methods=["POST"])
def create_user_route():
    data = request.get_json()
    email = data["email"]
    password = data["password"]
    repo = UserRepositorySQLite()
    user = create_user(email,password,repo)
    return jsonify(
		{
            "id" : user.id,		
            "email" : user.email,
		}
	)
    
@user_bp.route("/login", methods = ["POST"])
def login_route():
    data = request.get_json()
    repo = UserRepositorySQLite()
    user = login_user(data["email"], data["password"], repo)
    access_token = create_access_token(identity=user.email)
    return jsonify({"access_token":access_token})
        