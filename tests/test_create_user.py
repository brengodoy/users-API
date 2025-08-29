import pytest
import sqlite3
from application.create_user import create_user
from infrastructure.user_repository import UserRepositorySQLite
import bcrypt

@pytest.fixture
def repo():
    return UserRepositorySQLite(":memory:")

class TestCreateUser():
    def test_success(self, repo):
        email = "example@gmail.com"
        password = "password"
        user = create_user(email, password, repo)
        assert user.email == email
        assert bcrypt.checkpw(
            password.encode("utf-8"), 
            user.password_hash.encode("utf-8")
        )
        
    def test_invalid_email(self, repo):
        email = "noemail.comnoemail@noemail"
        password = "password"
        with pytest.raises(ValueError) as e:
            create_user(email, password, repo)
        assert "email is not valid" in str(e.value)
        
    def test_no_password(self, repo):
        email = "example@gmail.com"
        password = None
        with pytest.raises(ValueError) as e:
            create_user(email, password, repo)
        assert "Password can not be None." in str(e.value)
        
    def test_blank_password(self, repo):
        email = "example@gmail.com"
        password = ""
        with pytest.raises(ValueError) as e:
            create_user(email, password, repo)
        assert "Password can not be blank." in str(e.value)
        
    def test_space_password(self, repo):
        email = "example@gmail.com"
        password = " "
        with pytest.raises(ValueError) as e:
            create_user(email, password, repo)
        assert "Password can not be blank." in str(e.value)
        
    def test_duplicate_email(self, repo):
        email = "example1@gmail.com"
        password = "password"
        create_user(email, password, repo)
        with pytest.raises(sqlite3.IntegrityError) as e:
            create_user(email, password, repo)
        assert "UNIQUE constraint failed: users.email" in str(e.value)
        
    def test_no_repository(self):
        email = "example1@gmail.com"
        password = "password"
        with pytest.raises(ValueError) as e:
            create_user(email, password, None)
        assert "The repository cannot be None." in str(e.value)
        