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
    from flask import Flask
    app = Flask(__name__)

    # will be moved to "controller" file
    @app.route('/') # route to root directory
    def hello_world():
        return 'Hello World!'

    if __name__=="__main__": # MUST BE AT BOTTOM
        app.run(debug=True)
    ```
8. Test server
    ```
    python server.py
    ```