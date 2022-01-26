from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask import flash


class Recipe:
    def __init__( self , data):
        self.id = data['id']
        self.name = data['name']
        self.under_30_mins = data['under_30_mins']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    # Create
    @classmethod
    def create(cls,data:dict) -> int:
        query = "INSERT INTO recipes (name, under_30_mins, description, instructions, date_made, user_id) VALUES (%(name)s, %(under_30_mins)s, %(description)s, %(instructions)s, %(date_made)s, %(user_id)s);"
        user_id = connectToMySQL(DATABASE).query_db(query,data)
        return user_id

    # Retrieve
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(DATABASE).query_db(query)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes WHERE id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_one_by_email(cls, data):
        query = "SELECT * FROM recipes WHERE email=%(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False

    # Update
    @classmethod
    def update_one(cls, data):
        query = "UPDATE recipes SET name=%(name)s , under_30_mins=%(under_30_mins)s , description=%(description)s, instructions=%(instructions)s, date_made=%(date_made)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db( query, data )

    #Delete
    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db( query, data )

    #Validation
    @staticmethod
    def validate_recipe(data):
        is_valid = True

        if len(data['name']) < 3:
            flash("Recipe name must be 3 characters or longer.", 'err_name')
            is_valid = False
        if len(data['description']) < 3:
            flash("Recipe description must be 3 characters or longer.", 'err_description')
            is_valid = False
        if len(data['instructions']) < 3:
            flash("Recipe instructions must be 3 characters or longer.", 'err_instructions')
            is_valid = False
        if not data['date_made']:
            flash("You must choose a date that you made the recipe", 'err_date')
            is_valid = False
        if 'under_30_mins' not in data:
            flash("You must pick whether the recipe takes over or under 30 minutes to make", 'err_30_min')
            is_valid = False
        return is_valid