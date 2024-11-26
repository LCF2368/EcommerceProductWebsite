from flask import Flask

def create_app():
    app = Flask(__name__)
    # Configure the app (e.g., MongoDB setup)
    return app
