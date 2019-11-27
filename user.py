class User(object):
    def __init__(self, user: list):
        self.username = user[0]
        self.password = user[1]
        self.name = user[2]
        self.email = user[3]

    def to_collection(self):
        return {
            'username': self.username,
            'password': self.password,
            'name': self.name,
            'email': self.email,
        }
