from flask import request, render_template, redirect, url_for
from ..properties import ERRORS

def auth_error():
    code = request.args['code']
    return render_template('error.html', error=ERRORS[code])


def back_to_login():
  return redirect(url_for('general_login'))