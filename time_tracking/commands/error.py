from flask import request, render_template, redirect, url_for, session


def handle_404(error):
    return render_template('404.html', login=session.get('login')), 404


def handle_500(error):
    return render_template('500.html', login=session.get('login')), 500