import bcrypt
from domain.exceptions import UserNotFoundError, InvalidCredentialsError

def login_user(email, password, repo):
    try:
        user = repo.find_by_email(email)
        if bcrypt.checkpw(
            password.encode("utf-8"), 
            user.password_hash.encode("utf-8")
        ):
            return user
        else:
            raise InvalidCredentialsError("The password is not correct.")
    except AttributeError:
        raise UserNotFoundError("The entered email is not registered.")