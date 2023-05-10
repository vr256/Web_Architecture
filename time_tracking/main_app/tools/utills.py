from functools import wraps
from passlib.hash import sha512_crypt


def singleton(cls):
    obj = None
    @wraps(cls)
    def wrapper(*args, **kwargs):
        nonlocal obj
        if obj is None:
            obj = cls(*args, **kwargs)
        return obj
    return wrapper


def encrypt(password: str, key : str) -> str:
    '''
    Hashes given password by 
    key [should be login] via SHA-512
    '''
    rounds = 5000
    key = key.replace('_', '0')
    return sha512_crypt.using(salt=key, rounds=rounds).hash(password)