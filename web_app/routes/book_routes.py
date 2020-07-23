# web_app/routes/book_routes.py

from flask import Blueprint, jsonify, request, render_template

from web_app.models import Book, db,parse_records

book_routes = Blueprint("book_routes", __name__)


@book_routes.route("/books.json")
def list_books():
    book_records = Book.query.all()
    print(book_records)
    books = parse_records(book_records)
    return jsonify(books)

@book_routes.route("/books")
def list_books_for_humans():
    #books = [
    #{"id": 1, "title": "book 1"},
    #{"id": 2, "title": "book 2"},
    #{"id": 3, "title": "book 3"},
    #]
    book_records = Book.query.all()
    print(book_records)
    books = parse_records(book_records)
    return render_template("books.html", message="Some Books For You", books=books)

@book_routes.route("/books/new")
def new_book():
    return render_template("new_books.html")

@book_routes.route("/books/create", methods=["POST"])
def create_book():
    print("FORM DATA:", dict(request.form))

    new_book = Book(title=request.form["title"], author_id=request.form["author_name"])
    db.session.add(new_book)
    db.session.commit()

    return jsonify({
        "message": "book created",
        "book": dict(request.form)
    })


