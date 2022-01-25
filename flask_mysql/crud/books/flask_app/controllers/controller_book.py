from flask import render_template,  request, redirect, session
from flask_app import app
from flask_app.models import model_book, model_author

@app.route('/books')
def all_books():
    books = model_book.Book.get_all()
    return render_template('books.html', books=books)

@app.route('/books/<int:id>')
def show_book(id):
    book = model_book.Book.get_books_with_favorites({"id":id})
    all_authors = model_author.Author.get_all()
    return render_template('book_show.html',book=book, all_authors=all_authors)


@app.route('/books/create', methods=['POST'])
def create_book():
    # print(request.form)
    model_book.Book.create(request.form)
    return redirect('/books')

@app.route('/books/<int:id>/add_favorite', methods=['POST'])
def favorite_book(id):
    # print(request.form)
    model_author.Author.add_favorites({"author_id":request.form["author_id"],"book_id":id})
    return redirect(f'/books/{id}')