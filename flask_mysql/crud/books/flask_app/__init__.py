from flask import Flask

app = Flask(__name__)
app.secret_key = "gawsdfewagawe!-gagewa-adfgawe" # keep it secret keep it safe
DATABASE = "books_db"