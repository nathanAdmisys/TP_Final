from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("2ème route/")
def hello_world(je suis la deuxième route):
    return "<p>Hello, route2!</p>"
