# App
APP_VERSION = '1.1'
DBMS = 'MySQL'

# Logging
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
LOG_PATHES = {
    'time_tracking.commands.error' : 'time_tracking/logs/auth.txt',
    'time_tracking.commands.login' : 'time_tracking/logs/auth.txt',
    'time_tracking.commands.index' : 'time_tracking/logs/auth.txt',
    'time_tracking.connector' : 'time_tracking/logs/general.txt',
    'time_tracking.models.MDAO.maction_dao' : 'time_tracking/logs/DB.txt',
    'time_tracking.models.MDAO.mactivity_dao' : 'time_tracking/logs/DB.txt',
    'time_tracking.models.MDAO.mcategory_dao' : 'time_tracking/logs/DB.txt',
    'time_tracking.models.MDAO.mrole_dao' : 'time_tracking/logs/DB.txt',
    'time_tracking.models.MDAO.mtime_tracking_dao' : 'time_tracking/logs/DB.txt',
    'time_tracking.models.MDAO.muser_dao' : 'time_tracking/logs/DB.txt',
}

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