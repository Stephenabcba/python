from flask_app import app
from flask_app.controllers import controller_author, controller_book # IMPORT YOUR CONTROLLERS

if __name__=="__main__":
    app.run(debug=True)