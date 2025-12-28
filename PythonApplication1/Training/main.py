import UserDto
import UserHandler

print("Training module loaded successfully.")
u = UserDto.UserDto(id=1, username="john_doe", email="kki2020@daum.net",is_active=True)
u1 = UserDto.UserDto(id=2, username="jane_doe", email="aaa",is_active=True)
handler = UserHandler.UserHandler()
handler.add_user(u)
handler.add_user(u1)

active_users = handler.get_active_users()
print("Active Users:", active_users)
print("Active Users:", len(active_users))
