print("db_manager loaded")
import mysql.connector
from config import DB_CONFIG
from exceptions import *


class DBManager:
    def __init__(self):
        self.conn = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor(dictionary=True)

    def register_user(self, user):
        try:
            query = """INSERT INTO users (name, username, password, address)
                       VALUES (%s, %s, %s, %s)"""
            self.cursor.execute(query, (
                user.name, user.username, user.password, user.address
            ))
            self.conn.commit()
        except mysql.connector.errors.IntegrityError:
            raise UserAlreadyExistsError("Username already exists")

    def login(self, username, password):
        query = "SELECT * FROM users WHERE username=%s AND password=%s"
        self.cursor.execute(query, (username, password))
        user = self.cursor.fetchone()
        if not user:
            raise AuthenticationError("Invalid username or password")
        return user

    def change_password(self, user_id, new_password):
        query = "UPDATE users SET password=%s WHERE id=%s"
        self.cursor.execute(query, (new_password, user_id))
        self.conn.commit()

    def change_address(self, user_id, new_address):
        query = "UPDATE users SET address=%s WHERE id=%s"
        self.cursor.execute(query, (new_address, user_id))
        self.conn.commit()

    def delete_user(self, user_id):
        query = "DELETE FROM users WHERE id=%s"
        self.cursor.execute(query, (user_id,))
        self.conn.commit()
