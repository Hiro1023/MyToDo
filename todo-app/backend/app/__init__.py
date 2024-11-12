from flask import Flask, g
from routes import routes

app = Flask(__name__)
app.register_blueprint(routes)
