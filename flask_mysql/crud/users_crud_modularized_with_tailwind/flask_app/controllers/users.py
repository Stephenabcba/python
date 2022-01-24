from flask_app import app
from flask import render_template,  request, redirect, session
from flask_app.models.user import User

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/users')
def users():
    return render_template('index.html',users=User.get_all())

@app.route('/users/<int:id>')
def show_one(id):
    # users = User.get_all()
    # for user in users:
    #     if user.id == id:
    #         curUser = user
    #         break
    # return render_template('show.html',user = curUser)
    return render_template('show.html',user = User.get_one(id)[0])

@app.route('/users/<int:id>/edit')
def edit(id):
    # users = User.get_all()
    # for user in users:
    #     if user.id == id:
    #         curUser = user
    #         break
    # return render_template('edit.html',user=curUser)
    return render_template('edit.html',user=User.get_one(id)[0])

@app.route('/users/new')
def new_user():
    return render_template('create.html')


@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    new_user_id = User.save(data)
    return redirect(f'/users/{new_user_id}')

@app.route('/edit_user/<int:id>', methods=["POST"])
def edit_user(id):
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
        "id" : id,
    }
    User.update(data)
    return redirect(f'/users/{id}')

@app.route('/users/<int:id>/destroy')
def destroy_user(id):
    user=User.get_one(id)[0]
    data={"id":user.id}
    User.destroy(data)
    return redirect('/users')