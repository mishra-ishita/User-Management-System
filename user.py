class User:
    def __init__(self, name, username, password, address):
        self.name = name
        self.username = username
        self.password = password
        self.address = address

    def is_valid(self):
        if not self.name or not self.username or not self.password:
            return False
        return True
