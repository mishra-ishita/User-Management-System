class UserError(Exception):
    """Base exception for user-related errors"""
    pass

class UserNotFoundError(UserError):
    pass

class AuthenticationError(UserError):
    pass

class UserAlreadyExistsError(UserError):
    pass
