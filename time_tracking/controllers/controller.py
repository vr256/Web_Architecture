from flask import Flask, Request, render_template
from werkzeug.datastructures import ImmutableOrderedMultiDict
from ..config import APP_VERSION

class CustomRequest(Request):
    parameter_storage_class = ImmutableOrderedMultiDict

class App(Flask):
    request_class = CustomRequest

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_error_handler(404, self.my_404)

    def my_404(self, error):
        return render_template("404.html"), 404

    def make_response(self, rv):
        response = super().make_response(rv)
        response.headers['App-Version'] = APP_VERSION
        return response