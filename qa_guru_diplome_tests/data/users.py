import dataclasses


@dataclasses.dataclass
class User:
    name: str
    password: str
    email: str
