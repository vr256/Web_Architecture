from flask import current_app as app
from ..commands import login, index, back_to_login, \
                       sign_out, show_users, sign_up, \
                       handle_404, handle_500

# index
app.add_url_rule('/', view_func=index)

# auth
app.add_url_rule('/signin/', view_func=login, methods=['GET', 'POST'])
app.add_url_rule('/signin/', view_func=back_to_login, methods=['POST'])

app.add_url_rule('/signup/', view_func=sign_up, methods=['GET', 'POST'])

app.add_url_rule('/logout', view_func=sign_out, methods=['POST'])


# errors
app.errorhandler(404)(handle_404)
app.errorhandler(500)(handle_500)