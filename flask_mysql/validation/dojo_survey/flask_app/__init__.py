from flask import Flask
app = Flask(__name__)
app.secret_key = "I love surveys"

DATABASE = "dojo_survey_db"