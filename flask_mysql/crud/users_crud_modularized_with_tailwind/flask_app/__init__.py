from flask import Flask
app = Flask(__name__)
app.secret_key = "this_app_does_not_use_sessions"