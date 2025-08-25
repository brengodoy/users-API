from domain.user import User
from email_validator import validate_email, EmailNotValidError

def create_user(email : str, password : str, repo) -> User:
    valid_email = validate_email_address(email)
    hash = hash_password(password)
    user = User(valid_email,hash)
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