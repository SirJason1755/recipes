from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask_app.models.recipe import Recipe


@app.route('/recipes')
def user_recipe():
    data ={
        'users_id': session['user_id']
    }   
    recipes = Recipe.get_recipe(data)
    user = User.usersolo(data)

    return render_template('recipe.html',user = user, recipes = recipes)

@app.route('/recipes/create')
def create():

    return render_template('addrecipe.html')

@app.route('/recipes/new', methods = ['POST'])
def create_recipe():
    data = {
                'name':request.form['name'],
                'description':request.form['description'],
                'instructions':request.form['instructions'],
                'cooktime':request.form['cooktime'],
                'users_id': session['user_id']
    }
    Recipe.save_recipe(data)
    return redirect('/recipes')
        
@app.route('/recipes/view/<int:recipe_id>')
def render_recipe(recipe_id):
    data = {
        'id':recipe_id
    }
    recipe = Recipe.view_recipe(data)
    return render_template ('view.html', recipe = recipe)

@app.route('/recipes/edit/<int:recipe_id>')
def edit_recipe(recipe_id):
    data = {
        'id':recipe_id
    }
    recipe = Recipe.view_recipe(data)
    return render_template('edit.html',recipe = recipe)


@app.route('/recipes/update', methods = ['POST'])
def update_recipe():
    data ={
                'name':request.form['name'],
                'description':request.form['description'],
                'instructions':request.form['instructions'],
                'cooktime':request.form['cooktime'],
                'id':request.form['recipe_id'],
                'users_id':session['user_id']
    }
    Recipe.update_the_recipe(data)
    return redirect('/recipes')

@app.route('/recipes/delete/<int:recipe_id>')
def delete_recipe(recipe_id):
    data = {
        'id':recipe_id
    }
    Recipe.destroy(data)
    return redirect('/recipes')


