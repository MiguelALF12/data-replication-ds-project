from flask import jsonify
from ..models.user import User
from flask_jwt_extended import create_access_token


def create_user(username, email, password):
    new_user = User(username=username, email=email, password=password)
    user_id = new_user.save()
    return {"id": user_id, "username": username, "email": email}


def authenticate(username, password):
    user = User.validate_login(username, password)
    if user:
        return create_access_token(identity=str(user["_id"]))
    else:
        return None


def get_users():
    users = User.find_all()
    users_list = [{"id": str(user["_id"]), "username": user["username"],
                   "email": user["email"]} for user in users]
    return jsonify(users_list)


def get_user(user_id):
    user = User.find_one(user_id)
    if user:
        return jsonify({"id": str(user["_id"]), "username": user["username"], "email": user["email"]})
    else:
        return jsonify({"error": "User not found"}), 404


def update_user(user_id, username, email):
    result = User.update(user_id, {"username": username, "email": email})
    if result > 0:
        return jsonify({"message": "User updated"}), 200
    else:
        return jsonify({"error": "User not found"}), 404


def delete_user(user_id):
    result = User.delete(user_id)
    if result > 0:
        return jsonify({"message": "User deleted"}), 200
    else:
        return jsonify({"error": "User not found"}), 404
