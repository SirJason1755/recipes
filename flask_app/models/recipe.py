from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash





class Recipe():

    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.cooktime = data['cooktime'] == 1
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']
        self.users_id = data['users_id']

    @classmethod
    def get_recipe(cls,data):
        query = ("SELECT * FROM recipes WHERE users_id = %(users_id)s")
        recipe_from_db = connectToMySQL('my_recipes').query_db(query,data)
        recipe = []
        print(recipe_from_db,'gdhsgffda')
        for r in recipe_from_db:
            recipe.append(cls(r))
        return recipe

    @classmethod
    def save_recipe(cls,data):
        query = 'Insert INTO recipes (name,description,instructions,cooktime, users_id, created_at,updated_at) VALUES(%(name)s,%(description)s,%(instructions)s,%(cooktime)s, %(users_id)s ,NOW(),NOW());'
        add = connectToMySQL('my_recipes').query_db(query,data)
        return add

    @classmethod
    def view_recipe(cls,data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        view = connectToMySQL('my_recipes').query_db(query,data)
        result = view[0]
        getid = Recipe(result)
        return  getid

    @classmethod
    def update_the_recipe(cls,data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s,users_id = %(users_id)s,instructions=%(instructions)s,cooktime = %(cooktime)s,updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('my_recipes').query_db(query,data)


    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL('my_recipes').query_db(query,data)


    # @staticmethod
    # def validate_recipe(data):
    #     is_valid = True

    #     if len (data['name']) < 3 or len(data['name']) > 30:
    #         is_valid = False
    #         flash('Parameters not met')

    #     if len (data['description']) < 3 or len(data['description']) > 300:
    #         is_valid = False
    #         flash('Parameters not met')


    #     if len (data['instructions']) < 3 or len(data['instructions']) > 300:
    #         is_valid = False
    #         flash('Parameters not met')

