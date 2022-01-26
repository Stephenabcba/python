from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "3r5231240jgfawojdaffja329-aw" # keep it secret keep it safe
DATABASE = "recipes_db"
bcrypt = Bcrypt(app)