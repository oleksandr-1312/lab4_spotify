import mysql.connector

class UserDAO:
    def get_connection(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Rtyweq123464",
            database="spotify_lab3"
        )

    def get_all_users(self):
        conn = self.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        conn.close()
        return users

    def insert_user(self, username, email, reg_date):
        conn = self.get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO users (username, email, registration_date) VALUES (%s, %s, %s)"
        cursor.execute(sql, (username, email, reg_date))
        conn.commit()
        conn.close()

    def update_user(self, user_id, username, email):
        conn = self.get_connection()
        cursor = conn.cursor()
        sql = "UPDATE users SET username=%s, email=%s WHERE idusers=%s"
        cursor.execute(sql, (username, email, user_id))
        conn.commit()
        conn.close()

    #Видалення даних
    def delete_user(self, user_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        sql = "DELETE FROM users WHERE idusers=%s"
        cursor.execute(sql, (user_id,))
        conn.commit()
        conn.close()

    #Зв'язок 1:M (Усі плейлисти одного користувача)
    def get_user_playlists(self, user_id):
        conn = self.get_connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM playlists WHERE users_idusers=%s"
        cursor.execute(sql, (user_id,))
        playlists = cursor.fetchall()
        conn.close()
        return playlists

    #Зв'язок M:M (Усі пісні з конкретного плейлиста)
    def get_playlist_songs(self, playlist_id):
        conn = self.get_connection()
        cursor = conn.cursor(dictionary=True)
        sql = """
            SELECT s.song_id, s.title, s.duration_seconds 
            FROM songs s
            JOIN playlist_songs ps ON s.song_id = ps.songs_song_id
            WHERE ps.playlists_idplaylists = %s
        """
        cursor.execute(sql, (playlist_id,))
        songs = cursor.fetchall()
        conn.close()
        return songs