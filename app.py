from flask import Flask, jsonify  # сперва подключим модуль
from flask_sqlalchemy import SQLAlchemy
import os

path_sqldb = os.path.join(
        os.getenv('SYSTEMDRIVE'),
        r'\SQLite Stepik RestAPI\restapi.sqlite'
    )

app = Flask(__name__)  # объявим экземпляр фласка
# 'C:\SQLite Stepik RestAPI.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + path_sqldb
db = SQLAlchemy(app)

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)

    language = db.Column(db.String)
    pages = db.Column(db.Integer)

# db.create_all()
#
# books = []
#
# books.append(Book(
#     title="Python Crash Course",
#     author="Eric Matthes",
#     language="python",
#     pages=416
# ))
# books.append(Book(
#     title="Head First Python 2e",
#     author="Paul Barry",
#     language="python",
#     pages=215
# ))
# books.append(Book(
#     title="JavaScript: The Definitive Guide",
#     author="David Flanagan ",
#     language="javascript",
#     pages=812
# ))
#
# db.session.add_all(books)
# db.session.commit()
#
#
#
# @app.route('/')
# def render_main():
#     return 'Здесь будет главная'
#
#
# @app.route('/products/')
# def render_products():
#     return 'Продукты'

@app.route('/about/')
def render_about():
    return 'Информация о проекте'


# @app.route('/book/<author>/<title>/')
# def render_book(author, title):
#     return "Здесь будет страница книги " + title + " автора " + author


# @app.route('/books/<int:book_id>/')
# def render_book(book_id):
#     print(type(book_id))
#     return ""

@app.route("/books/<int:id>", methods=["GET"])
def api_get(id):
    book_id= id
    #  получаем объект книжки
    book = db.session.query(Book).get(book_id)
    if book:
        # переводим объект в словарь
        book_dict = dict(id=book_id, title=book.title, author=book.author, language=book.language, pages=book.pages)
        # возвращаем словарь, если объект нашелся
        return jsonify(book_dict)
    # возвращаем 404, если нет
    return jsonify(), 404


@app.route('/temp/<float:temp_value>/')
def render_temp(temp_value):
    print(type(temp_value))
    return ""


# @app.errorhandler(404)
# def render_not_found(error):
#     return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!"
#
#
# @app.errorhandler(500)
# def render_server_error(error):
#     return "Что-то не так, но мы все починим"




app.run()  # запустим сервер
