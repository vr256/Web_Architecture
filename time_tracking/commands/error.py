import logging

from flask import request, render_template, redirect, url_for
from ..config import ERRORS, LOG_FORMAT, LOG_PATHES

logging.basicConfig(level=logging.DEBUG, filename=LOG_PATHES[__name__], 
                    filemode="a+", format=LOG_FORMAT)

def auth_error():
    code = request.args['code']
    return render_template('error.html', error=ERRORS[code])


def back_to_login():
  return redirect(url_for('general_login'))