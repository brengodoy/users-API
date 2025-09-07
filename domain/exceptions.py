class CustomError(Exception):
    status_code = 400
    
    def __init__(self, message):
        super().__init__(message)
        self.message = message or "An error occurred."

class UserEmailAlreadyExists(CustomError):
    status_code = 409
    
class EnteredEmailNotValidError(CustomError):
    status_code = 422
    
class NoRespositoryError(CustomError):
    status_code = 500
    
class UserNotFoundError(CustomError):
    status_code = 404
    
class InvalidCredentialsError(CustomError):
    status_code = 422