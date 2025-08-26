import sqlite3
from domain.user import User

class UserRepositorySQLite():
    def __init__(self, db_path = "users.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.create_table()
    
    def create_table(self):
        with self.conn as conn:
            cursor = conn.cursor()
            sql = """CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE,
                password TEXT)"""
            cursor.execute(sql)
            conn.commit()
    
    def save(self, user):
        with self.conn as conn:
            cursor = conn.cursor()
            sql = """INSERT INTO users (email,password) VALUES (?,?)"""
            cursor.execute(sql, (user.email, user.password_hash))
            conn.commit()
            user.id = cursor.lastrowid
    
    def find_by_email(self,email):
        with self.conn as conn:
            cursor = conn.cursor()
            sql = """SELECT * FROM users WHERE email = ?"""
            cursor.execute(sql,(email,))
            row = cursor.fetchone()
            if row:
                return User(user_id = row[0],email = row[1], password_hash = row[2])
            return None