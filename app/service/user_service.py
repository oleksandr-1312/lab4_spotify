from app.dao.user_dao import UserDAO

class UserService:
    def __init__(self):
        self.dao = UserDAO()
        
    def get_all(self):
        return self.dao.get_all_users()
        
    def create_user(self, data):
        # Отримуємо дані від контролера і передаємо в DAO
        self.dao.insert_user(data['username'], data['email'], data['registration_date'])
        
    def update_user(self, user_id, data):
        self.dao.update_user(user_id, data['username'], data['email'])

    def delete_user(self, user_id):
        self.dao.delete_user(user_id)

    def get_user_playlists(self, user_id):
        return self.dao.get_user_playlists(user_id)

    def get_playlist_songs(self, playlist_id):
        return self.dao.get_playlist_songs(playlist_id)