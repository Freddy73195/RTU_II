# Создать класс Store. Поля: название магазина, адрес, коллекция аудиодисков (список экземпляров класса Audio),
#     коллекция фильмов (список экземпляров класса DVD). Определить конструктор. Переопределить метод преобразования
#     в строку для печати всей информации о магазине (с использованием переопределения в классах Audio и DVD).
#     Переопределить методы получения количества дисков функцией len, получения диска по индексу, изменения по
#     индексу, удаления по индексу (пусть вначале идут индексы аудиодисков, затем фильмов). Переопределить
#     операции + и - для добавления или удаления диска. Добавить функцию создания txt-файла и записи всей
#     информации в него (в том числе списков песен и главных ролей фильма).
# Предусмотреть хотя бы в 3 местах обработку возможных исключений.

import pickle
from datetime import datetime

import audio
import dvd
from audio import Audio
from dvd import DVD
class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.audio_collection = []
        self.dvd_collection = []
        self.log_event("CRE", f"Создан объект |{name}| класса Store")
    def __str__(self):
        s = f"{self.name}\n{self.address}\n\nAudio collection:\n"
        for audio in self.audio_collection:
            s += str(audio) + "\n"
        s += "\nDVD collection:\n"
        self.log_event("INF", f"Был произведён вывод всей музыкальной продукции магазина")
        for dvd in self.dvd_collection:
            s += str(dvd) + "\n"
        self.log_event("INF", f"Был произведён вывод всей кино продукции магазина")
        return s
    def __len__(self):
        self.log_event("INF", f"Был произведён вывод колличества продукции в магазине")
        return len(self.audio_collection) + len(self.dvd_collection)
    def __getitem__(self, index):
        if index < len(self.audio_collection):
            self.log_event("INF", f"Было произведёно получение информации о продукте по его номеру в магазине")
            return self.audio_collection[index]
        else:
            return self.dvd_collection[index - len(self.audio_collection)]
    def __setitem__(self, index, value):
        if index < len(self.audio_collection):
            self.audio_collection[index] = value
        else:
            self.dvd_collection[index - len(self.audio_collection)] = value
    def __delitem__(self, index):
        if index < len(self.audio_collection):
            del self.audio_collection[index]
        else:
            del self.dvd_collection[index - len(self.audio_collection)]
    # def add_disk(self, disk):
    #     if isinstance(disk, Audio):
    #         self.audio_collection.append(disk)
    #     elif isinstance(disk, DVD):
    #         self.dvd_collection.append(disk)
    #     else:
    #         raise TypeError("The disk must be an instance of Audio or DVD")

    def __add__(self, disk): # +
        if isinstance(disk, Audio):
            self.audio_collection.append(disk)
            self.log_event("INF", f"Было произведёно добавление музыкального продукта в магазин")
        elif isinstance(disk, DVD):
            self.dvd_collection.append(disk)
            self.log_event("INF", f"Было произведёно добавление кино продукта в магазин")
        else:
            raise TypeError("The disk must be an instance of Audio or DVD")
        return self

    # def remove_disk(self, disk):
    #     if isinstance(disk, Audio):
    #         if disk in self.audio_collection:
    #             self.audio_collection.remove(disk)
    #         else:
    #             raise ValueError("The audio disk is not in the collection")
    #     elif isinstance(disk, DVD):
    #         if disk in self.dvd_collection:
    #             self.dvd_collection.remove(disk)
    #         else:
    #             raise ValueError("The DVD disk is not in the collection")
    #     else:
    #         raise TypeError("The disk must be an instance of Audio or DVD")

    def __sub__(self, disk): # -
        if isinstance(disk, Audio):
            if disk in self.audio_collection:
                self.audio_collection.remove(disk)
                self.log_event("INF", f"Было произведёно удаление |{disk}|")
            else:
                self.log_event("ERR", f"Попытка удаления |{disk}|. Ошибка! |{disk}| отсутствует в списке")
                raise ValueError("The audio disk is not in the collection")
        elif isinstance(disk, DVD):
            if disk in self.dvd_collection:
                self.dvd_collection.remove(disk)
                self.log_event("INF", f"Было произведёно удаление |{disk}|")
            else:
                self.log_event("ERR", f"Попытка удаления |{disk}|. Ошибка! |{disk}| отсутствует в списке")
                raise ValueError("The DVD disk is not in the collection")
        else:
            raise TypeError("The disk must be an instance of Audio or DVD")
        return self

    # def __sub__(self, disk): # -
    #     if isinstance(disk, Audio):
    #         if disk in self.audio_collection:
    #         #     self.audio_collection.remove(disk)
    #         #     self.log_event("INF", f"Было произведёно удаление |{disk}|")
    #         # else:
    #         #     self.log_event("ERR", f"Попытка удаления |{disk}|. Ошибка! |{disk}| отсутствует в списке")
    #         #     raise ValueError("The audio disk is not in the collection")
    #             try:
    #                 self.audio_collection.remove(disk)
    #             except FileNotFoundError:
    #                 self.log_event("ERR", f"Попытка удаления |{disk}|. Ошибка! |{disk}| отсутствует в списке")
    #             # self.log_event("INF", f"Было произведёно удаление |{disk}|")
    #             # except FileNotFoundError:


        # elif isinstance(disk, DVD):
        #     if disk in self.dvd_collection:
        #         self.dvd_collection.remove(disk)
        #         self.log_event("INF", f"Было произведёно удаление |{disk}|")
        #     else:
        #         self.log_event("ERR", f"Попытка удаления |{disk}|. Ошибка! |{disk}| отсутствует в списке")
        #         raise ValueError("The DVD disk is not in the collection")
        # else:
        #     raise TypeError("The disk must be an instance of Audio or DVD")
        # return self

    def create_txt_file(self, filename):
        self.log_event("INF", f"Был создан файл с информацией о магазине и его продукцией")
        with open(filename, "w") as f:
            f.write(f"{self.name}\n{self.address}\n\nМузыкальная коллекция:\n")
            for audio in self.audio_collection:
                f.write(str(audio) + "\n")
                f.write("Песни:\n")
                for song, duration in audio.songs.items():
                    f.write(f"{song} - {duration}\n")
            f.write("\nКоллекция кино:\n")
            for dvd in self.dvd_collection:
                f.write(str(dvd) + "\n")
                f.write("Роли:\n")
                for role, actor in dvd.roles.items():
                    f.write(f"{role} - {actor}\n")


    def log_event(self, key, comment):  # делаем лог действия
        with open("log.txt", "a", encoding="utf-8") as f:
            now = datetime.now()
            date_time = now.strftime("%d/%m/%Y %H:%M:%S")
            f.write(f"{key} --- {date_time} --- {comment}\n")

def store_test():
    Store1 = Store("GStop", "г.Москва ул.Проспект Вернадского д.78 ИВЦ")
    Store1.__add__ = (audio.Disk)
    Store1.__add__ = (dvd.Disk)
    try:
        Store1 -= Store1[0]

    except AssertionError:
        print("Test Error")
    else:
        print("Test Passed")

# # Создаем экземпляры класса Person
# Store1 = Store("GStop", "г.Москва ул.Проспект Вернадского д.78 ИВЦ")
# Store1.__add__ = (audio.Disk)
# Store1.__add__ = (dvd.Disk)
#
# # Сериализуем экземпляры в файл
# with open("stores.pkl", "wb") as f:
#     pickle.dump([Store1], f)