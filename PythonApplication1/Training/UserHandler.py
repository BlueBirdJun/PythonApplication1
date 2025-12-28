import UserDto



class UserHandler:
    def __init__(self,):
        self.users = []
    def add_user(self, user: UserDto.UserDto):
        self.users.append(user)
    def get_active_users(self):
        return [user for user in self.users if user.is_active]