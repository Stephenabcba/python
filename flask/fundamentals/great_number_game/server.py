from flask import Flask, render_template,  request, redirect, session
from random import randint
from re import match

app = Flask(__name__)
app.secret_key = "this is a great number game"

# will be moved to "controller" file
@app.route('/') # route to root directory
def hello_world():
    if "target_number" not in session:
        session["target_number"] = randint(1,100)
        session["result"] = None
    return render_template("index.html")

@app.route('/guess', methods=["POST"])
def guess():
    # print(request.form)
    guess_num = request.form["guess"]
    if match("[-+]?\d+$", guess_num):
        guess_num = int(guess_num)
        if guess_num > session["target_number"]:
            session["result"] = "High"
        elif guess_num < session["target_number"]:
            session["result"] = "Low"
        else:
            session["result"] = "correct"
    else:
        session["result"] = "invalid"
    return redirect("/")

@app.route('/restart', methods=["POST"])
def restart():
    session.clear()
    return redirect("/")

if __name__=="__main__": # MUST BE AT BOTTOM
    app.run(debug=True)