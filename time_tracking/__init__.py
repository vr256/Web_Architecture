from flask import Flask
from .factory import DB_Factory

app = Flask(__name__)
app.config['dbms'] = 'mysql'
app.config['db'] = DB_Factory.get_db(app.config['dbms'])
app.config['db'].connect()
app.app_context().push()

from .views import user_session