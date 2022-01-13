from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<int:rows>")
@app.route("/<int:rows>/<int:cols>")
@app.route("/<int:rows>/<int:cols>/<color1>")
@app.route("/<int:rows>/<int:cols>/<color1>/<color2>")
def checkerBoard(rows=8,cols=8,color1='black',color2='red'):
    return render_template("index.html",rows=rows,cols=cols,color1=color1,color2=color2)



if __name__ == "__main__":
    app.run(debug=True)