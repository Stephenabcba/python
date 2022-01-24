from flask_app.config.mysqlconnection import MySQLConnection
from flask_app import DATABASE
from flask import flash

class User:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['name']) < 1:
            flash("Name cannot be blank")
            is_valid = False
        if len(data['location']) < 1:
            flash("Location cannot be blank")
            is_valid = False
        if len(data['language']) < 1:
            flash("Language cannot be blank")
            is_valid = False
        if len(data['comment']) < 1:
            flash("Comment cannot be blank")
            is_valid = False
        return is_valid