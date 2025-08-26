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
        return email_info.email
    except EmailNotValidError as e:
        raise ValueError(str(e))

def hash_password(password : str) -> str:
    pass