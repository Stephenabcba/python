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
    ```
    pipenv install flask pyMySQL
    ```
    ```
    pipenv install flask pyMySQL flask-bcrypt
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
9. 1: File Structure with MySQL database connection, modularized
    ```
    - Main_app
        - flask_app
            - config
                - mysqlconnection.py
            - controllers
                - controller_table_name.py
            - models
                - models_model_name.py
            - static
                - img
                - css
                    - style.css
                - js
            - templates
                - index.html
            - __init__.py
        - pipfile
        - pipfile.lock
        - server.py
    ```
    - server.py MUST IMPORT ALL CONTROLLERS FOR THEM TO WORK


10. Test server inside pipenv shell
    ```
    python server.py
    ```
11. mysqlconnection.py file (does not need editing)
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
12. model_table_name.py file (will need to rename table name)
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
13. In model python file (create, call the database, return)
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
                users.append(cls(user))
            return users

        @classmethod
        def get_one(cls, data):
            query = "SELECT * FROM users WHERE id=%(id)s;"
            results = connectToMySQL(DATABASE).query_db(query, data)
            if results:
                return cls(results[0])
            return False

        # U
        @classmethod
        def update_one(cls, data):
            query = "UPDATE users SET first_name=%(fname)s , last_name=%(lname)s , email=%(email)s WHERE id = %(id)s;"
            return connectToMySQL(DATABASE).query_db( query, data )

        #D
        @classmethod
        def delete_one(cls, data):
            query = "DELETE FROM users WHERE id = %(id)s;"
            return connectToMySQL(DATABASE).query_db( query, data )

    ```
14. RESTful naming techniques for controller route names
    ```
    /table_name : display: all entries in table
    /table_name/new : display: form to create a new entry into table
    /table_name/create : action: take the form from '/new' to create the entry
    /table_name/<id> : display: entry with id of id
    /table_name/<id>/edit: display: form to edit entry with id
    /table_name/<id>/update: action: take the form from '/edit' and update the entry
    /table_name/<id>/delete: delete the specific entry
    ```

15. Regular Expression email validation
    ```py
    import re
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

    EMAIL_REGEX.match(data['email'])
    ```

16. Rendering Flashed messages in html
    - https://flask.palletsprojects.com/en/1.0.x/patterns/flashing/
    ```html
    {% with messages = get_flashed_messages() %}   <!-- declare a variable called messages -->
        {% if messages %}              <!-- check if there are any messages -->
            {% for message in messages %}      <!-- loop through the messages -->
                <p>{{message}}</p>          <!-- display each message in a paragraph tag -->
            {% endfor %}
        {% endif %}
    {% endwith %}
    ```

17. Bcrypt (done in controller file)
    ```py
    from flask_bcrypt import Bcrypt
    bcrypt = Bcrypt(app)

    # in creating / updating the password
    bcrypt.generate_password_hash(password_string) 

    # in login verification
    bcrypt.check_password_hash(hashed_password, password_string)
    ```

18. Updated server.py
19. __init__.py
    ```py
    from flask import Flask
    app = Flask(__name__)
    app.secret_key = "keep it secret keep it safe"
    DATABASE = "database_name"
    ```
- Useful stuff
    - convert the form from POST into a dictionary, with an extra key-value pair of id
    ```py
    data = {
        **request.form,
        "id": id
    }
    ```
    - passing just id as data dictionary (anonymous dictionary)
    ```py
    get_one({"id",id})
    ```
    - get the entry B related to foreign key of entry A (done in model_A.py)
      - method one: 
          - JOIN A to B using A.foreign_key = B.key
          - create object A using results from query
          - create data dict using results (we have to rename B.id to id, etc)
            - create object B using data dict
          - add B as an attribute to A (A.b_name = instance_B)
          - return A
      - method two:
          - utilize get_one method of B
          - A get_one() using given id
            - B get_one(), using A.foreign_key_to_B
            - in A:
            ```py
                @property
                def B_name(self):
                    return B.get_one(A.foreign_key_to_B)
            ```
            - to use it: (property decorator eliminates the parenthesis)
            ```py
            instance_A.B_name # returns an instance of B, do object instance attribute calls as needed for B
            ```

- Info:
    - if importing a model from another model, import the whole model.py file
        - prevents circular importing
        - in controller files, it's ok to import only the class from the model file