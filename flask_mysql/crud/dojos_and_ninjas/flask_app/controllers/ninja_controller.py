from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

@app.route('/ninjas')
def ninjas():
    return render_template("ninja.html",dojos=Dojo.get_all())

@app.route('/ninjas/create',methods=["POST"])
def create_ninja():
    # print(request.form)
    Ninja.insert(request.form)
    return redirect(f'/dojos/{request.form["dojo_id"]}')