# Создать класс Disk с полями название, жанр, цена. Добавить конструктор класса.
from datetime import datetime
class Disk:
    def __init__(self, name, genre, price):
        self.name = name
        self.genre = genre
        self.price = price

    def log_event(self, key, comment):  # делаем лог действия
        with open("log.txt", "a", encoding="utf-8") as f:
            now = datetime.now()
            date_time = now.strftime("%d/%m/%Y %H:%M:%S")
            f.write(f"{key} --- {date_time} --- {comment}\n")