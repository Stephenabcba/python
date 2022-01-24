from flask_app import app
from flask_app.controllers import controller_user


if __name__=="__main__": # MUST BE AT BOTTOM
    app.run(debug=True)