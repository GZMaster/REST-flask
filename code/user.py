class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        return cls.find_by_username(username)

    @classmethod
    def find_by_id(cls, _id):
        return cls.find_by_id(_id)
