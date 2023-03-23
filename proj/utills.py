import functools
import bcrypt

def singleton(cls):
    obj = None
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        nonlocal obj
        if obj is None:
            obj = cls(*args, **kwargs)
        return obj
    return wrapper

def encode(password: str):
    '''
    Hashes given password using bcrypt
    '''
    byte_str = password.encode('utf-8')
    salt = bcrypt.gensalt()
    byte_pass = bcrypt.hashpw(byte_str, salt)
    return byte_pass.decode('utf-8')