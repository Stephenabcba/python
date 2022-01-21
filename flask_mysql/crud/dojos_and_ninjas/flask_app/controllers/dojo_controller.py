from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojo_model import Dojo

@app.route('/')
def root():
    return redirect('/dojos')


@app.route('/dojos')
def dojos():
    return render_template("dojo.html",dojos_list=Dojo.get_all())


@app.route('/dojos/<int:id>')
def dojos_show(id):
    id_data = {"id":id}
    dojo=Dojo.get_ninjas_of_dojo(id_data)
    # print(dojo.ninjas[0].first_name)
    return render_template("dojo_show.html",dojo=dojo)


@app.route('/dojos/create',methods=['POST'])
def create_dojo():
    Dojo.insert(request.form)
    return redirect('/dojos')

@app.route('/dojos/delete/<int:id>')
def delete_dojo(id):
    id_dict = {'id':id}
    Dojo.delete_one(id_dict)
    return redirect('/dojos')

