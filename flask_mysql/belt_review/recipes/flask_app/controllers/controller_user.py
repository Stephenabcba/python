from flask import render_template,  request, redirect, session
from flask_app import app, bcrypt
from flask_app.models import model_user, model_recipe

@app.route('/')
def entry():
    if 'uuid' in session:
        return redirect('/dashboard')
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'uuid' not in session:
        return redirect('/')
    recipes = model_recipe.Recipe.get_all()
    return render_template('dashboard.html', recipes=recipes)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/register', methods=['POST'])
def register():
    print(request.form)
    is_valid = model_user.User.validate_register(request.form)
    if not is_valid:
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'pw': pw_hash
    }
    session['uuid'] = model_user.User.create(data)
    session['first_name'] = data['first_name']
    session['email'] = data['email']
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    is_valid = model_user.User.validate_login(request.form)
    if not is_valid:
        return redirect('/')
    user = model_user.User.get_one_by_email(request.form)
    session['uuid'] = user.id
    session['first_name'] = user.first_name
    session['email'] = user.email
    return redirect('/dashboard')