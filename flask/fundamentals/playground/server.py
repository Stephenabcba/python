from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def load_page():
    return render_template("index.html")

@app.route('/play/<int:block_count>')
def load_x_blocks(block_count):
    return render_template("index.html", block_count = block_count)

@app.route('/play/<int:block_count>/<string:color>')
def load_x_colored_blocks(block_count,color):
    return render_template("index.html", block_count = block_count, color=color)

if __name__ == __name__:
    app.run(debug=True)