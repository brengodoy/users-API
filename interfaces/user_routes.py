from flask import request, jsonify, Blueprint
from infrastructure.user_repository import UserRepositorySQLite
from application.create_user import create_user

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