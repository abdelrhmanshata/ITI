import os
from flask import Flask
from flask import request, render_template, redirect, url_for, flash
from datetime import datetime
from werkzeug.utils import secure_filename


# configure flask _sql alchemy

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # initialize the application in the main of the current module


# connect flask app to the database (ORM===> object relational mapper )
"sqllite_"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["UPLOAD_FOLDER"] = (
    "D:\\Project\\Flask\\bookStoreApp\\static\\bookImages\\"  # Folder to store uploaded images
)
db = SQLAlchemy(app)  # create instance folder---> contain project.db


# use db object ---> create model ---> used later in create table and crud
class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    details = db.Column(db.String)
    pages = db.Column(db.Integer)
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    image = db.Column(db.String, default="book.png")

    def __str__(self):
        return f"{self.title}/{self.details}"


## create model in the db


# books = [
#     {
#         "id": 1,
#         "title": "Book1",
#         "details": "Details Book1Details Book1Details Book1Details Book1Details Book1Details Book1Details Book1Details Book1Details Book1Details Book1Details Book1Details Book1Details Book1Details Book1Details Book1Details Book1Details Book1Details Book1",
#         "numOfPage": 100,
#         "price": 150,
#         "create_at": "2024-02-18 2:30 PM",
#         "update_at": "2024-02-18 2:30 PM",
#         "image": "book.png",
#     },
#     {
#         "id": 2,
#         "title": "Book2",
#         "details": "Details Book1",
#         "numOfPage": 100,
#         "price": 150,
#         "create_at": "2024-02-18 2:30 PM",
#         "update_at": "2024-02-18 2:30 PM",
#         "image": "book.png",
#     },
#     {
#         "id": 3,
#         "title": "Book3",
#         "details": "Details Book1",
#         "numOfPage": 100,
#         "price": 150,
#         "create_at": "2024-02-18 2:30 PM",
#         "update_at": "2024-02-18 2:30 PM",
#         "image": "book.png",
#     },
#     {
#         "id": 4,
#         "title": "Book4",
#         "details": "Details Book1",
#         "numOfPage": 100,
#         "price": 150,
#         "create_at": "2024-02-18 2:30 PM",
#         "update_at": "2024-02-18 2:30 PM",
#         "image": "book.png",
#     },
#     {
#         "id": 5,
#         "title": "Book5",
#         "details": "Details Book1",
#         "numOfPage": 100,
#         "price": 150,
#         "create_at": "2024-02-18 2:30 PM",
#         "update_at": "2024-02-18 2:30 PM",
#         "image": "book.png",
#     },
#     {
#         "id": 6,
#         "title": "Book6",
#         "details": "Details Book1",
#         "numOfPage": 100,
#         "price": 150,
#         "create_at": "2024-02-18 2:30 PM",
#         "update_at": "2024-02-18 2:30 PM",
#         "image": "book.png",
#     },
#     {
#         "id": 7,
#         "title": "Book7",
#         "details": "Details Book1",
#         "numOfPage": 100,
#         "price": 150,
#         "create_at": "2024-02-18 2:30 PM",
#         "update_at": "2024-02-18 2:30 PM",
#         "image": "book.png",
#     },
# ]

#


@app.route("/", endpoint="home")
def home():
    books = Book.query.all()
    return render_template("books/home.html", books=books)


@app.route("/show-book/<int:id>", endpoint="book.show")
def show_book(id):
    book = Book.query.get_or_404(id)
    # book = Book.query.get(id)
    if book:
        return render_template("books/show_book.html", book=book)

    error = "Book Not Found"
    return render_template("error/error.html", error=error)


@app.route("/books/add", methods=["GET", "POST"], endpoint="book.add")
def add_book():
    if request.method == "POST":
        title = request.form["title"]
        details = request.form["details"]
        pages = request.form["pages"]
        price = request.form["price"]
        image = request.files["image"]

        book = Book(title=title, details=details, pages=int(pages), price=int(price))
        if image:
            imageName = secure_filename(image.filename)
            image.save(os.path.join(app.config["UPLOAD_FOLDER"], imageName))
            book.image = imageName

        db.session.add(book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("books/add_book.html")


@app.route("/update-book/<int:id>", endpoint="book.update", methods=["GET", "POST"])
def update_book(id):
    book = Book.query.get_or_404(id)
    if request.method == "POST":
        book.title = request.form["title"]
        book.details = request.form["details"]
        book.price = int(request.form["price"])
        book.pages = int(request.form["pages"])

        image = request.files["image"]
        if image:
            imageName = secure_filename(image.filename)
            image.save(os.path.join(app.config["UPLOAD_FOLDER"], imageName))
            book.image = imageName

        db.session.commit()

        db.session.commit()
        return redirect(url_for("home"))
    else:
        if book:
            return render_template("books/update_book.html", book=book)
    return render_template("error/error.html")


@app.route("/delete-book/<int:id>", endpoint="book.delete", methods=["GET"])
def delete_book(id):
    book = Book.query.get_or_404(id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for("home"))

    error = "Book Not Found"
    return render_template("error/error.html", error=error)


@app.errorhandler(404)
def get_404(error):
    return render_template("error/error.html", error=error)


if __name__ == "__main__":
    # run the  development server
    app.run(debug=True, port=5000)
