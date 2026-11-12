from flask import Blueprint, request, jsonify
from app.service.user_service import UserService

user_bp = Blueprint('user_controller', __name__)
service = UserService()

@user_bp.route('/users', methods=['GET'])
def get_users():
    return jsonify(service.get_all())

@user_bp.route('/users', methods=['POST'])
def add_user():
    data = request.json
    service.create_user(data)
    return jsonify({"message": "Користувача успішно додано!"}), 201

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    service.update_user(user_id, data)
    return jsonify({"message": "Дані користувача оновлено!"})


@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    service.delete_user(user_id)
    return jsonify({"message": "Користувача видалено!"})

#Вивід 1:M (Плейлисти конкретного користувача)
@user_bp.route('/users/<int:user_id>/playlists', methods=['GET'])
def get_user_playlists(user_id):
    return jsonify(service.get_user_playlists(user_id))

#Вивід M:M (Пісні в конкретному плейлисті)
@user_bp.route('/playlists/<int:playlist_id>/songs', methods=['GET'])
def get_playlist_songs(playlist_id):
    return jsonify(service.get_playlist_songs(playlist_id))