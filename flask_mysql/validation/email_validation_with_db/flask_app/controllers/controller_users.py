from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import model_user

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/register', methods=["POST"])
def register():
    if not model_user.User.validate_email(request.form):
        return redirect ('/')
    model_user.User.create(request.form)
    return redirect('/success')

@app.route('/success')
def success():
    emails = model_user.User.get_all()
    return render_template('success.html', emails=emails)

@app.route('/delete/<int:id>')
def delete(id):
    model_user.User.delete_one({'id':id})
    return redirect('/success')