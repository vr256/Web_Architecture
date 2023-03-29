APP_VERSION = '1.1'

# DB config
POOL_SIZE = 5
POOL_NAME = 'pool'
db_config = {
    'user': 'root',
    'password': '123456',
    'host': '127.0.0.1',
    'database': 'time_tracking_db'
}

# Routing
ROUTES = {
    '': '',
}

# Errors
ERRORS = {
    'AUTH_CRED': 'No user with such login or email found',
    'AUTH_PASS': 'Wrong password',
}