from flask import Flask, Request
from werkzeug.datastructures import ImmutableOrderedMultiDict

from ..properties import APP_VERSION

class MyRequest(Request):
    parameter_storage_class = ImmutableOrderedMultiDict

class App(Flask):
    request_class = MyRequest

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def make_response(self, rv):
        response = super().make_response(rv)
        response.headers['App-Version'] = APP_VERSION
        return response