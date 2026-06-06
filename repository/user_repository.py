from models.user_models import user
class UserRepository:
    def __init__(self):
        self.users = []

    def add_user(self, user_data: user):
        self.users.append(user_data)

    def get_user(self, user_id: int):
        for user in self.users:
            if user.id == user_id:
                return user
        return None
    def get_all_users(self):
        return self.users