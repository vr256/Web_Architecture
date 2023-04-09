from flask import request, render_template, redirect, url_for
from ..properties import ERRORS

def auth_error():
    code = request.args['code']
    return render_template('error.html', error=ERRORS[code])

def handle_404(error):
    return render_template('404.html'), 404

def handle_500(error):
    return render_template('500.html'), 500

def back_to_login():
  return redirect(url_for('general_login'))