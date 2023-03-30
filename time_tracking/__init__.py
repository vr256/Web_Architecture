from .controllers.controller import App
from .factory import DB_Factory
from .config import DBMS

app = App(__name__)
app.config['dbms'] = DBMS
app.config['db'] = DB_Factory.get_db(app.config['dbms'])
app.config['db'].connect()
app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=True)
app.app_context().push()

# needed for routing
from .controllers import controller_helper