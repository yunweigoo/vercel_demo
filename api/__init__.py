from flask import Blueprint, jsonify

api = Blueprint('api', __name__)

@api.route('/')
def api_home():
    return jsonify({"message": "Welcome to the API!"})

@api.route('/hello')
def api_hello():
    return jsonify({"message": "Hello, API!"})

@api.route('/user')
def api_user():
    user_data = {"id": 1, "name": "John Doe", "email": "johndoe@example.com"}
    return jsonify(user_data)
