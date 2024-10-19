from flask import Blueprint, request, jsonify
from app.auth.auth import SECRET_KEY
import jwt
from functools import wraps  # Импортируем wraps

secrets_blueprint = Blueprint('secrets', __name__)

# Example in-memory secret store
SECRET_STORE = {}

def token_required(f):
    @wraps(f)  # Используем wraps для сохранения имени функции
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except:
            return jsonify({'message': 'Token is invalid!'}), 403
        return f(*args, **kwargs)
    return decorated_function

@secrets_blueprint.route('/store', methods=['POST'])
@token_required
def store_secret():
    data = request.get_json()
    secret_key = data.get('key')
    secret_value = data.get('value')
    SECRET_STORE[secret_key] = secret_value
    return jsonify({'message': 'Secret stored successfully'}), 201

@secrets_blueprint.route('/retrieve/<key>', methods=['GET'])
@token_required
def retrieve_secret(key):
    secret_value = SECRET_STORE.get(key)
    if secret_value:
        return jsonify({'secret': secret_value}), 200
    return jsonify({'message': 'Secret not found'}), 404
