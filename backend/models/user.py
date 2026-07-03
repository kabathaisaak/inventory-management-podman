class User:

    def __init__(
        self,
        id,
        username,
        password,
        role,
        created_at
    ):
        self.id = id
        self.username = username
        self.password = password
        self.role = role
        self.created_at = created_at

    def to_dict(self):

        return {
            "id": self.id,
            "username": self.username,
            "role": self.role,
            "created_at": self.created_at
        }