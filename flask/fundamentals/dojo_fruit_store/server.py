from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    cur_time = datetime.now().strftime("%B %d %Y %X %p")
    return render_template("checkout.html",strawberry=int(request.form["strawberry"]), raspberry=int(request.form["raspberry"]),apple=int(request.form["apple"]), first_name=request.form["first_name"], last_name=request.form["last_name"], student_id=request.form["student_id"],cur_time = cur_time)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)