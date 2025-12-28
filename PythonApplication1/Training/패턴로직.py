# Repository (DB 접근 계층)
class UserRepository:
    def __init__(self):
        # 실제 DB 대신 메모리
        self._users = {
            1: UserDto(1, "kim"),
            2: UserDto(2, "lee"),
        }

    def get_by_id(self, user_id: int) -> UserDto | None:
        return self._users.get(user_id)

    def save(self, user: UserDto) -> None:
        self._users[user.id] = user

# Service (비즈니스 로직)
class UserService:
    def __init__(self, repo: UserRepository):
        self._repo = repo

    def rename_user(self, user_id: int, new_name: str) -> UserDto:
        user = self._repo.get_by_id(user_id)
        if not user:
            raise ValueError("User not found")

        user.name = new_name
        self._repo.save(user)
        return user

# 사용 예 (Controller 느낌)
repo = UserRepository()
service = UserService(repo)

updated = service.rename_user(1, "park")
print(updated)

# public / private 없음 (관례만 있음)
class A:
    def __init__(self):
        self.public = 1
        self._protected = 2   # 관례
        self.__private = 3    # name mangling
