from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

books_blueprint = Blueprint("books", __name__)


# ----- MVP -----

# INDEX
@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books = books)


# DELETE
@books_blueprint.route("/books/<id>/delete", methods=['post'])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')

# ----- EXTENSIONS -----

# SHOW


# NEW
@books_blueprint.route("/books/new", methods=["GET"])
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", all_authors = authors)





# @tasks_blueprint.route('/tasks/new', methods=['GET'])
# def new_task():
#     users = user_repository.select_all()
#     return render_template('tasks/new.html', users = users)

# CREATE





# ----- ADVANCED EXTENSIONS -----

# EDIT


# UPDATE




