from flask_app.config.mysqlconnetion import connectToMySQL
from flask_app.models.ninja_model import Ninja

DATABASE = "dojos_and_ninjas_db"
class Dojo:
    def __init__(self,data) -> None:
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    # C
    @classmethod
    def insert(cls, data)->int:
        query = "INSERT INTO dojos(name) VALUES (%(name)s);"
        dojo_id = connectToMySQL(DATABASE).query_db(query,data)
        return dojo_id

    # Retrieve
    @classmethod
    def get_all(cls)->list:
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        dojos_list = []
        for dojo in results:
            dojos_list.append(cls(dojo))
        return dojos_list

    @classmethod
    def get_one(cls,id)->dict:
        query = "SELECT * FROM dojos WHERE id=%(id)s;"
        return cls(connectToMySQL(DATABASE).query_db(query,id)[0])

    @classmethod
    def get_ninjas_of_dojo(cls,id)->list:
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,id)
        dojo = cls(results[0])
        # print(dojo)
        for ninja in results:
            if ninja['ninjas.id']:
                data = {
                    'id':ninja['ninjas.id'],
                    'first_name':ninja['first_name'],
                    'last_name':ninja['last_name'],
                    'age':ninja['age'],
                    'created_at':ninja['ninjas.created_at'],
                    'updated_at':ninja['ninjas.updated_at']
                }
                dojo.ninjas.append(Ninja(data))
        return dojo

    # Update
    @classmethod
    def update_one(cls,data_with_id)->None:
        query = "UPDATE dojos SET name=%(name)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data_with_id)

    # Delete
    @classmethod
    def delete_one(cls,id:dict)->None:
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,id)

