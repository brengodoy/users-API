class User():
    def __init__(self, email, password_hash, user_id = None):
        self.id = user_id
        self.email = email
        self.password_hash = password_hash
        
    def set_new_password(self, password):
        self.password_hash = password
        
    def check_password(self, raw_password):
        pass
        