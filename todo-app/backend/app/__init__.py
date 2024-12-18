from flask import Flask, g
from flask_cors import CORS
from routes import routes

app = Flask(__name__)
app.register_blueprint(routes)
CORS(app)