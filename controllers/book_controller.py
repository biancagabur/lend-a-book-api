from flask import jsonify, request
from models.book import Book
from controllers import books_bp
from models import db


@books_bp.route('/books', methods=['GET'])
def get_books():
    title = request.args.get('title')
    if title:
        books = Book.query.filter(Book.title.ilike(f'%{title}%')).all()
        if not books:
            return jsonify({'message': 'Book not found'}), 404
    else:
        books = Book.query.all()
    books_list = [book.to_dict() for book in books]
    return jsonify(books_list)


@books_bp.route('/books/<string:title>', methods=['GET'])
def get_book(title):
    # Retrieve a book by title
    book = Book.query.filter_by(title=title).first()
    if book:
        return jsonify(book.to_dict())
    else:
        return jsonify({'message': 'Book not found'}), 404


@books_bp.route('/books/<string:title>', methods=['PUT'])
def update_book(title):
    # Update an existing book by title
    book = Book.query.filter_by(title=title).first()
    if book:
        data = request.get_json()
        author = data.get('author')
        book.author = author
        db.session.commit()
        return jsonify({'message': 'Book updated successfully'})
    else:
        return jsonify({'message': 'Book not found'}), 404


@books_bp.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')

    # Check if a book with the same title already exists
    existing_book = Book.query.filter_by(title=title).first()
    if existing_book:
        return jsonify({'message': 'Book already exists'}), 409

    # Create and add the book if it doesn't exist
    book = Book(title=title, author=author)
    db.session.add(book)
    db.session.commit()
    return jsonify({'message': 'Book created successfully', 'id': book.id}), 201


@books_bp.route('/books/<string:title>', methods=['DELETE'])
def delete_book(title):
    # Delete a book by title
    book = Book.query.filter_by(title=title).first()
    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify({'message': 'Book deleted successfully'})
    else:
        return jsonify({'message': 'Book not found'}), 404