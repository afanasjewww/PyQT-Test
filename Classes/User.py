class User:
    def __init__(self, login, password, name, surname):
        self.login = login
        self.password = password
        self.name = name
        self.surname = surname

    def to_dict(self):
        return {
            "login": self.login,
            "password": self.password,
            "name": self.name,
            "surname": self.surname
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            login = data["login"],
            password=data["password"],
            name=data["name"],
            surname=data["surname"]
        )
