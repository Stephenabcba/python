from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return("Hello World!")

@app.route('/dojo')
def dojo():
    return("Dojo!")

@app.route('/say/<word>')
def say(word):
    return(f"Hi {word.title()}!")

@app.route('/repeat/<int:times>/<string:word>')
def repeat(times, word):
    return (word * times)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.