from typing import TypedDict


class LoginCredentials(TypedDict):
    """
    Typed dictionary representing login credentials.

    Attributes:
        username: The username.
        password: The password.

    """
    username: str
    password: str
