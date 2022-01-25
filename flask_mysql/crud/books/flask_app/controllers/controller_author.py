from flask import render_template,  request, redirect, session
from flask_app import app
from flask_app.models import model_author, model_book

@app.route('/')
def root_route():
    return redirect('/authors')

@app.route('/authors')
def authors():
    authors = model_author.Author.get_all()
    return render_template('index.html',authors=authors)

@app.route('/authors/<int:id>')
def author_show(id):
    author = model_author.Author.get_author_with_favorites({"id":id})
    books = model_book.Book.get_all()
    return render_template('author_show.html', author=author, books=books)


@app.route('/authors/create', methods=['POST'])
def create_author():
    # print(request.form)
    model_author.Author.create(request.form)
    return redirect('/authors')

@app.route('/authors/<int:id>/add_favorite', methods=['POST'])
def add_favorite(id):
    # print(request.form)
    model_author.Author.add_favorites({"author_id":id,"book_id":request.form["book_id"]})
    return redirect(f'/authors/{id}')

