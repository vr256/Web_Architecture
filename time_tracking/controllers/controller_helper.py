from flask import current_app as app
from ..commands import general_login, general_index, auth_error, \
                       back_to_login, logout, show_users

app.add_url_rule('/login/', view_func=general_login, methods=['GET', 'POST'])
app.add_url_rule('/login/', view_func=back_to_login, methods=['POST'])

app.add_url_rule('/logout', view_func=logout, methods=['POST'])
app.add_url_rule('/error/', view_func=auth_error)

app.add_url_rule('/', view_func=show_users, methods=['POST'])
app.add_url_rule('/', view_func=general_index)