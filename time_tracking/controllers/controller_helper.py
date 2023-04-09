from flask import current_app as app
from ..commands import general_login, general_index, auth_error, \
                       back_to_login, logout, show_users, enter_data, \
                       handle_404, handle_500

# index
app.add_url_rule('/', view_func=general_index)

# sign in
app.add_url_rule('/login/', view_func=general_login, methods=['GET', 'POST'])
app.add_url_rule('/login/', view_func=back_to_login, methods=['POST'])
app.add_url_rule('/logout', view_func=logout, methods=['POST'])

# sign up
app.add_url_rule('/signup/', view_func=enter_data)

# errors
app.errorhandler(404)(handle_404)
app.errorhandler(500)(handle_500)