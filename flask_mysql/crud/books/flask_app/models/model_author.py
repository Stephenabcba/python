from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import model_book


class Author:
    def __init__( self , data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    # Create
    @classmethod
    def create(cls,data:dict) -> int:
        query = "INSERT INTO authors (name) VALUES (%(name)s);"
        user_id = connectToMySQL(DATABASE).query_db(query,data)
        return user_id

    # Retrieve
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL(DATABASE).query_db(query)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM authors WHERE id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False
    
    @classmethod
    def get_author_with_favorites(cls, data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id=favorites.author_id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        print(results[0])
        if not results:
            return False
        if not results[0]['books.id']:
            return cls(results[0])
        author = cls(results[0])
        author.favorite_books = []
        author.favorite_ids = []
        for entry in results:
            data = {
                **entry,
                "id":entry['books.id']
            }
            book = model_book.Book(data)
            author.favorite_books.append(book)
            author.favorite_ids.append(book.id)
            print(book.id)
        return author

    # Update
    @classmethod
    def update_one(cls, data):
        query = "UPDATE authors SET name=%(name)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db( query, data )

    #Delete
    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM authors WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db( query, data )

    @staticmethod
    def add_favorites(data):
        query = "INSERT INTO favorites (book_id, author_id) VALUES (%(book_id)s, %(author_id)s)"
        return connectToMySQL(DATABASE).query_db( query, data)