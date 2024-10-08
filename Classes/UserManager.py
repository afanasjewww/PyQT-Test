import json
import os

from Classes.User import User


class UserManager:
    def __init__(self, file_path):
        self.file_path = file_path



    def save_user(self, user):
        users = self._load_users()
        users.append(user.to_dict())

        with open(self.file_path, 'w') as f:
            json.dump(users, f, indent=4)



    def _load_users(self):
        if not os.path.exists(self.file_path):
            return []

        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                if isinstance(data, list):
                    return data
                else:
                    return []
        except (json.JSONDecodeError, FileNotFoundError):
            return []



    def load_user(self):
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                return [User.from_dict(user) for user in data]
        except FileNotFoundError:
            print("No user data found")
            return []



    def user_exists(self, login):
        users = self._load_users()

        for user_data in users:
            if user_data.get("login") == login:
                return True
        return False


    def validate_user(self, login, password):
        users = self._load_users()

        for user_data in users:
            if user_data.get("login") == login and user_data.get("password") == password:
                return True
            return False