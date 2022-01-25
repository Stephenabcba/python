from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app, DATABASE
import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class User:
    def __init__(self,data) -> None:
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



    @classmethod
    def create(cls,data:dict) -> int:
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        user_id = connectToMySQL(DATABASE).query_db(query,data)
        return user_id

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL(DATABASE).query_db(query)
        emails = []
        for email in results:
            emails.append(cls(email))
        return emails

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM emails WHERE id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_one_by_email(cls, data):
        query = "SELECT * FROM emails WHERE email=%(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False
    
    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(DATABASE).query_db( query, data )




    @staticmethod
    def validate_email(data) -> bool:
        is_valid = True
        if not EMAIL_REGEX.match(data['email']) :
            flash("Please enter a valid email address")
            is_valid = False
        elif User.get_one_by_email(data):
            flash("The email already exists!")
            is_valid = False
        return is_valid

