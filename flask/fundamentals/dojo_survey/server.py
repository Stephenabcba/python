from flask import Flask, render_template,  request, redirect, session
app = Flask(__name__)
app.secret_key = "I love surveys"

@app.route('/')
def index_page():
    return render_template("index.html")

@app.route('/process',methods=["POST"])
def process():
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comment"] = request.form["comment"]
    session["courseType"] = request.form["courseType"]
    if "promo_email" in request.form:
        session["promo_email"] = "Yes"
    else:
        session["promo_email"] = "No"
    # print(request.form)
    return redirect('/result')


@app.route('/result')
def result():
    return render_template("result.html")

@app.route('/return', methods=["POST"])
def return_to_index():
    session.clear()
    return redirect('/')

if __name__=="__main__": # MUST BE AT BOTTOM
    app.run(debug=True)