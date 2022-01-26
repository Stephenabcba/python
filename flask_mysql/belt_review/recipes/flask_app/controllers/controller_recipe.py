from flask import render_template,  request, redirect, session
from flask_app import app, bcrypt
from flask_app.models import  model_recipe
from datetime import datetime


@app.route('/recipes/new')
def recipe_new():
    if 'uuid' not in session:
        return redirect('/')
    return render_template('recipe_new.html')

@app.route('/recipes/create', methods=["POST"])
def recipe_create():
    if 'uuid' not in session:
        return redirect('/')
    if not model_recipe.Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    data = {
        **request.form,
        "user_id":session["uuid"]
    }
    model_recipe.Recipe.create(data)
    return redirect('/dashboard')


@app.route('/recipes/<int:id>')
def recipe_show(id):
    if 'uuid' not in session:
        return redirect('/')
    recipe = model_recipe.Recipe.get_one({"id":id})
    recipe.date_made = recipe.date_made.strftime("%B %d, %Y")
    return render_template('recipe_show.html',recipe=recipe)

@app.route('/recipes/edit/<int:id>')
def recipe_edit(id):
    if 'uuid' not in session:
        return redirect('/')
    recipe = model_recipe.Recipe.get_one({"id":id})
    if recipe.user_id == session['uuid']:
        return render_template('recipe_edit.html',recipe=recipe)
    return redirect('/dashboard')

@app.route('/recipes/<int:id>/update', methods=["POST"])
def recipe_update(id):
    if 'uuid' not in session:
        return redirect('/')
    if not model_recipe.Recipe.validate_recipe(request.form):
        return redirect(f'/recipes/edit/{id}')
    recipe = model_recipe.Recipe.get_one({"id":id})
    if recipe.user_id == session['uuid']:
        data = {
            **request.form,
            "user_id":session["uuid"],
            "id":id
        }
        model_recipe.Recipe.update_one(data)
    return redirect('/dashboard')

@app.route('/recipes/<int:id>/delete')
def recipe_delete(id):
    if 'uuid' not in session:
        return redirect('/')
    recipe = model_recipe.Recipe.get_one({"id":id})
    if recipe.user_id == session['uuid']:
        model_recipe.Recipe.delete_one({"id":id})
    return redirect('/')
