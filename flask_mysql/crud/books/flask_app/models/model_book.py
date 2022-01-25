from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import model_author


class Book:
    def __init__( self , data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    # Create
    @classmethod
    def create(cls,data:dict) -> int:
        query = "INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s);"
        book_id = connectToMySQL(DATABASE).query_db(query,data)
        return book_id

    # Retrieve
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL(DATABASE).query_db(query)
        books = []
        for book in results:
            books.append(cls(book))
        return books

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM books WHERE id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_books_with_favorites(cls, data):
        query = "SELECT * FROM books LEFT JOIN favorites ON favorites.book_id = books.id LEFT JOIN authors ON authors.id=favorites.author_id WHERE books.id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        if not results[0]['authors.id']:
            return cls(results[0])
        book = cls(results[0])
        book.author_favorite = []
        book.favorite_ids = []
        for entry in results:
            data = {
                **entry,
                "id":entry['authors.id']
            }
            author = model_author.Author(data)
            book.author_favorite.append(author)
            book.favorite_ids.append(author.id)
        return book

    # Update
    @classmethod
    def update_one(cls, data):
        query = "UPDATE books SET title=%(title)s , num_of_pages=%(num_of_pages)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db( query, data )

    #Delete
    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM books WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db( query, data )