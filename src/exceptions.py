from fastapi import HTTPException, status


class UserNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"}
        )



class CredentialsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )


class InvalidRoleException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Role",
            headers={"WWW-Authenticate": "Bearer"})


class NotSuperadminException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Siz super admin emassiz ",
            headers={"WWW-Authenticate": "Bearer"})


class UsernameException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Bunday username orqali foydalanuvchi avval royxatdan otgan ",
            headers={"WWW-Authenticate": "Bearer"})

class SecurityException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Qandaydir xatolik roy berdi ",
            headers={"WWW-Authenticate": "Bearer"})


class NotUsernameException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Bunday username orqali foydalanuvchi royxatda mavjud emas ",
            headers={"WWW-Authenticate": "Bearer"})