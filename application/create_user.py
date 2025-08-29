from domain.user import User
from email_validator import validate_email, EmailNotValidError
from infrastructure.user_repository import UserRepositorySQLite
import bcrypt
import sqlite3
from domain.exceptions import UserEmailAlreadyExists,EnteredEmailNotValidError,NoRespositoryError

def create_user(email : str, 
                password : str, 
                repo : UserRepositorySQLite) -> User:
    valid_email = validate_email_address(email)
    password_hash = hash_password(password)
    user = User(valid_email, password_hash)
    if repo:
        try:
            repo.save(user)
        except sqlite3.IntegrityError:
            raise UserEmailAlreadyExists("The email already exists.")
    else:
        raise NoRespositoryError("The repository cannot be None.")
    return user

def validate_email_address(email : str) -> str:
    try:
        email_info = validate_email(email)
        return email_info.normalized
    except EmailNotValidError:
        raise EnteredEmailNotValidError("Email is not valid.")

def hash_password(password : str) -> str:
    if password is not None:
        if not password.isspace() and password:
            hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
            return hashed.decode("utf-8")
        else:
            raise ValueError("Password can not be blank.")
    else:
        raise ValueError("Password can not be None.")