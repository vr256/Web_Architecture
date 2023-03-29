from flask import Flask

app = Flask(__name__)
app.dbms = 'mysql'
app.app_context().push()

from .views import user_session