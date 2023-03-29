import logging

from flask import request, render_template, redirect, url_for, session
from ..properties import ERRORS

logging.basicConfig(level=logging.DEBUG, filename="../logfile.txt", filemode="a+",
                    format="%(asctime)-15s %(levelname)-8s %(message)s")


def auth_error():
    code = request.args['code']
    return render_template('error.html', error=ERRORS[code])


def back_to_login():
  return redirect(url_for('general_login'))