import os
from os.path import join, dirname, realpath

import flask_login
from flask import Flask
from flask_mongoengine import MongoEngine
# import pymongo
# from pymongo.server_api import ServerApi


ALLOWED_EXTENSIONS = {'png', 'jpeg', 'jpg'}
INPUT_FILENAME = ''


app = Flask(__name__, template_folder='./templates')
app.config['MONGODB_SETTINGS'] = {
    'host': ""
}
db = MongoEngine(app)
app.config['SECRET_KEY'] = ''
app.config['UPLOAD_FOLDER'] = join(dirname(realpath(__file__)), 'static\\uploads\\')
app.config['MAX_CONTENT_LENGTH'] = 128 * 1024 * 1024
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

from backend import routes
