import os

from .controllers import App
from .tools import DB_Factory
from .properties import DBMS

app = App(__name__)
app.config['dbms'] = DBMS
app.config['db'] = DB_Factory.get_db(app.config['dbms'])
app.config['db'].connect()
app.config['SECRET_KEY'] = os.urandom(20).hex()
app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=True)
app.app_context().push()

from .controllers import controller_helper