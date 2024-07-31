from sqlite3 import connect, Connection, Cursor, Row

"""Создаем подключение к базе данных"""

con = connect("static/db/travaler.db")
cursor = Cursor(con)


"""Класс для работы с БД"""
class BooksDB:
    """"Инициализация атрибутов класса"""
    def __init__(self, connection: Connection) -> None: 
        self.__connection = connection
        self.__cursor = Cursor(connection)
        self.__cursor.row_factory = Row

    """Функция, возвращающая все данные из таблицы в БД"""
    def get_all_items(self):
        sql = "SELECT * FROM travel"
        try:
            self.__cursor.execute(sql)
            return self.__cursor.fetchall()
        except:
            print("Ошибка в базе данных")
            return []
        
    """Функция, возвращающая бронирование по ID"""    
    def getBookById(self, id:int) -> dict | None:
        sql = 'SELECT coordinates, sea_name, description, price, img_1,img_2 FROM travel WHERE id = ?'
        try:
            self.__cursor.execute(sql,(id,))
            return self.__cursor.fetchone()
        except:
            print("Море не найдено")
            return None