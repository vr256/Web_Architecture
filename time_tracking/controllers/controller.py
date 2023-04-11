from flask import Flask, Request, render_template
from ..properties import APP_VERSION


class App(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def make_response(self, rv):
        response = super().make_response(rv)
        response.headers['App-Version'] = APP_VERSION
        return response