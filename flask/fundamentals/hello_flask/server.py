from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template("index.html")  # Return the string 'Hello World!' as a response


# import statements, maybe some other routes
    
@app.route('/success')
def success():
    return "success"
    
    # app.run(debug=True) should be the very last statement! 

@app.route('/repeat/<string:name>/<int:num>')
def hello(name,num):
    return render_template("hello.html",name=name,num=num)

@app.route('/users/<username>/<int:id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + str(id +54321)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.