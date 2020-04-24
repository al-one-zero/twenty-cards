from flask import Flask
import os

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    try:
        os.makedirs(app.instance_path)
    except OSError as e:
        print(e)

    @app.route('/')
    def home():
        return '<h1>Hi</h1>'

    return app
