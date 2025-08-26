from domain.user import User
from email_validator import validate_email, EmailNotValidError
from infrastructure.user_repository import UserRepositorySQLite

def create_user(email : str, password : str, repo : UserRepositorySQLite) -> User:
    valid_email = validate_email_address(email)
    password_hash = hash_password(password)
    user = User(valid_email, password_hash)
    repo.save(user)
    return user

def validate_email_address(email : str) -> str:
    try:
        email_info = validate_email(email)
        return email_info.normalized
    except EmailNotValidError:
        raise ValueError("email is not valid")

def hash_password(password : str) -> str:
    if password is not None:
        if not password.isspace() and password:
            pass
        else:
            raise ValueError("Password can not be blank.")
    else:
        raise ValueError("Password can not be None.")