from flask import Flask, render_template,  request, redirect, session
from random import randint
from datetime import datetime
app = Flask(__name__)
app.secret_key = "I love gold"

@app.route('/')
def hello_world():
    if "money" not in session:
        session["money"] = 0
    if "moves" not in session:
        session["moves"] = 0
    return render_template("index.html")

@app.route('/process_money',methods=["POST"])
def process_money():
    if "action_log" not in session:
        session["action_log"] = []
    action = request.form["choice"]
    value_change = 0
    actions_list = {
        "farm": [10,20],
        "cave": [5,10],
        "house": [2,5],
        "casino": [-50,50],
        None : [0,0]
    }
    # if action not in actions_list:
    #     action = None
    # if action == "farm":
    #     value_change = randint(10,20)
    # elif action == "cave":
    #     value_change = randint(5,10)
    # elif action == "house":
    #     value_change = randint(2,5)
    # elif action == "casino":
    #     value_change = randint(-50,50)
    value_change = randint(actions_list[action][0],actions_list[action][1])
    message = ""
    if value_change > 0:
        message += "<p class='profit'>"
        message += f"Earned {value_change} golds from the {action}!"
    elif value_change == 0:
        message += "<p>"
        message += f"You earned nothing from the {action}."
    elif value_change < 0:
        message += "<p class='loss'>"
        message += f"Entered a {action} and lost {value_change} golds... Ouch.."
    message += f"({datetime.now().strftime('%Y/%m/%d %I:%M %p')})"
    message += "</p>"
    session["action_log"] = [message] + session["action_log"]
    session["money"] += value_change
    session["moves"] += 1
    print(f"Location: {action}, Income: {value_change}")
    return redirect("/")

@app.route('/reset',methods=["POST"])
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)