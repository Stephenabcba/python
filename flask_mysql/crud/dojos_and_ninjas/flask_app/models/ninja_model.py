from this import d
from flask_app.config.mysqlconnetion import connectToMySQL
DATABASE = "dojos_and_ninjas_db"
class Ninja:
    def __init__(self,data) -> None:
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]

    # C
    @classmethod
    def insert(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s,%(age)s,%(dojo_id)s)"
        return connectToMySQL(DATABASE).query_db(query,data)