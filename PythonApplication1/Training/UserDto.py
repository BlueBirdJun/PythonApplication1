from dataclasses import dataclass


@dataclass
class UserDto:
     id: int
     username: str
     email: str
     is_active: bool 