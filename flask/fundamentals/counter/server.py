from flask import Flask, render_template,  request, redirect, session

app = Flask(__name__)

app.secret_key = "this is my secret key"

@app.route('/')
def counter():
    if "counter" not in session or "visit_count" not in session:
        session["visit_count"] = 1
        session["counter"] = 1
    else:
        session["visit_count"] += 1
        session["counter"] += 1
    return render_template("index.html")

@app.route('/reset',methods=['POST'])
@app.route('/destroy_session')
def destroy_session():
    # if "counter" in session:
    #     session.pop("counter")
    session.clear()
    return redirect('/')

@app.route('/plus_n',methods=['POST'])
def plus_n():
    session["counter"] += int(request.form["increment_amount"]) -1
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)