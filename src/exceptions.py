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
            detail="Bunday  foydalanuvchi avval royxatdan otgan ",
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
            detail="Bunday username orqali foydalanuvchi royxatda mavjud emas",
            headers={"WWW-Authenticate": "Bearer"})



class NotTokenException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="token yaroqsiz yoki muddato otgan",
            headers={"WWW-Authenticate": "Bearer"})

class DepartmentException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Bu department allaqochon mavjud ",
            headers={"WWW-Authenticate": "Bearer"})



class NotDepartmentException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Bo'lim mavjud emas",
            headers={"WWW-Authenticate": "Bearer"})


class NotDeviceException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Qurilma mavjud emas",
            headers={"WWW-Authenticate": "Bearer"})




class TokenExpiredException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token Expired Exception",
            headers={"WWW-Authenticate": "Bearer"}
        )


class TokenExpiredException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token Expired Exception",
            headers={"WWW-Authenticate": "Bearer"}
        )


class UserLoggedOutException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User logged out",
            headers={"WWW-Authenticate": "Bearer"}
        )