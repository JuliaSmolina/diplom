from flask import Flask, render_template, g
import sqlite3
import base

"""Создание объект класса Flask, настраиваем конфигурацию"""
app = Flask(__name__)
app.config['DATABASE'] = "static/db/travaler.db"
app.secret_key = 'Pluto'

"""Подключение к БД"""
def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    return con

"""Создание уникального подключения"""
def get_connect():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db

"""Прерывание подключения"""
@app.teardown_appcontext
def close_connect(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()

"""Переменная, хранящая в себе данные для навигационной панели"""
navMenu = [
    {"link": "/index", "name": "Главная"}
]

"""Рендеринг (отрисовка) главной страницы"""
@app.route("/index/")
@app.route("/")
def index():
    booksObject = base.BooksDB(get_connect())
    lst = booksObject.get_all_items()
    return render_template("index.html", menu = navMenu,cardList=lst)

"""Рендеринг (отрисовка) страницы бронирования"""
@app.route("/books/<int:id>")
def show_book(id:int):
    booksObject = base.BooksDB(get_connect())
    result = booksObject.getBookById(id)
    if result:
        return render_template("thebook.html", book=result,menu = navMenu,)
    else:
        return "Нет моря"

"""Запуск приложения"""
if __name__ == "__main__":
    app.run()