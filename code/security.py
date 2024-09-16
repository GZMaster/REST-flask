from user import User
import hmac

users = [
    User(1, "admin", "admin"),
    User(2, "user", "user"),
]


username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and hmac.compare_digest(
        user.password.encode("utf-8"), password.encode("utf-8")
    ):
        return user
    return None


def identity(payload):
    user_id = payload["identity"]
    return userid_mapping.get(user_id, None)
