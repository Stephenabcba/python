# Pre-Req
```
pip install pipenv
```
# Creating a flask project from scratch

1. create a folder for project / assignment
2. go into that folder
3. open a terminal in that folder
4. create a virtual Env
    ```
    pipenv install flask
    ```
    - more dependencies if needed
    - if it doesn't work:
    ```
    python -m pipenv [command]
    ```
5. check for pipfile and pipfile.lock
    1. WARNING: if these don't exit, then figure it out
        - you might have pipenv in parent directory
6. Activate our virtual Environment
    ```
    pipenv shell
    ```
    - to exit:
        ```
        exit
        ```
7. Create server.py file
    ```py
    from flask import Flask, render_template,  request, redirect, session
    app = Flask(__name__)

    # will be moved to "controller" file
    @app.route('/') # route to root directory
    def hello_world():
        return 'Hello World!'

    if __name__=="__main__": # MUST BE AT BOTTOM
        app.run(debug=True)
    ```
8. Create file structure
    - Main_app
        - server.py
        - pipfile
        - pipfile.lock
        - templates
            - index.html
        - static
            - img
            - css
            - js
8. 1: File Structure with MySQL database connection
    - Main_app
        - server.py
        - mysqlconnection.py
        - models
            - models_model_name.py
        - pipfile
        - pipfile.lock
        - templates
            - index.html
        - static
            - img
            - css
                - style.css
            - js


9. Test server inside pipenv shell
    ```
    python server.py
    ```
10. mysqlconnection.py file
    ```py
    # a cursor is the object we use to interact with the database
    import pymysql.cursors
    # this class will give us an instance of a connection to our database
    class MySQLConnection:
        def __init__(self, db):
            # change the user and password as needed
            connection = pymysql.connect(host = 'localhost',
                                        user = 'root', 
                                        password = 'root', 
                                        db = db,
                                        charset = 'utf8mb4',
                                        cursorclass = pymysql.cursors.DictCursor,
                                        autocommit = True)
            # establish the connection to the database
            self.connection = connection
        # the method to query the database
        def query_db(self, query, data=None):
            with self.connection.cursor() as cursor:
                try:
                    query = cursor.mogrify(query, data)
                    print("Running Query:", query)
        
                    cursor.execute(query)
                    if query.lower().find("insert") >= 0:
                        # INSERT queries will return the ID NUMBER of the row inserted
                        self.connection.commit()
                        return cursor.lastrowid
                    elif query.lower().find("select") >= 0:
                        # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                        result = cursor.fetchall()
                        return result
                    else:
                        # UPDATE and DELETE queries will return nothing
                        self.connection.commit()
                except Exception as e:
                    # if the query fails the method will return FALSE
                    print("Something went wrong", e)
                    return False
                finally:
                    # close the connection
                    self.connection.close() 
    # connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
    def connectToMySQL(db):
        return MySQLConnection(db)
    ```
11. model_table_name.py file
    ``` py
    # import the function that will return an instance of a connection
    from mysqlconnection import connectToMySQL
    # model the class after the friend table from our database
    class Friend:
        def __init__( self , data ):
            self.id = data['id']
            self.first_name = data['first_name']
            self.last_name = data['last_name']
            self.occupation = data['occupation']
            self.created_at = data['created_at']
            self.updated_at = data['updated_at']
        # Now we use class methods to query our database
        @classmethod
        def get_all(cls):
            query = "SELECT * FROM friends;"
            # make sure to call the connectToMySQL function with the schema you are targeting.
            results = connectToMySQL('first_flask').query_db(query)
            # Create an empty list to append our instances of friends
            friends = []
            # Iterate over the db results and create instances of friends with cls.
            for friend in results:
                friends.append( cls(friend) )
            return friends
    ```
12. In model python file (create, call the database, return)
    - Create: create()
    - Retrieve: get(), get_one()
    - Update: update_one()
    - Delete: delete_one()
    ```py
    from mysqlconnection import connectToMySQL

    DATABASE = 'users_db'

    class User:
        def __init__( self , data):
            self.id = data['id']
            self.first_name = data['first_name']
            self.last_name = data['last_name']
            self.email = data['email']
            self.created_at = data['created_at']
            self.updated_at = data['updated_at']
        
        # C
        @classmethod
        def create(cls,data:dict) -> int:
            query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
            user_id = connectToMySQL(DATABASE).query_db(query,data)
            return user_id

        # R
        @classmethod
        def get_all(cls):
            query = "SELECT * FROM users;"
            results = connectToMySQL(DATABASE).query_db(query)
            users = []
            for user in results:
                users.append(cls(results))
            return users

        @classmethod
        def get_one(cls):
            pass

        # U
        @classmethod
        def update_one(cls):
            pass

        #D
        @classmethod
        def delete_one(cls):
            pass
    ```