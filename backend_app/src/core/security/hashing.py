from passlib.context import CryptContext

# bcrypt is secure industry standard hashing algorithm
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str) -> str:
    """
    Converts plain password → hashed password
    """
    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    """
    Checks if password matches hash
    """
    return pwd_context.verify(
        plain_password,
        hashed_password
    )
