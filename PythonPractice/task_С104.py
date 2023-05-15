"""
Каждый класс реализовать в отдельном модуле, импортируя их в производные модули.
Создать класс Disk с полями название, жанр, цена. Добавить конструктор класса.
Создать производный от Disk класс Audio. Новые поля: исполнитель, студия звукозаписи, список песен (словарь вида
    название песни: длительность). Определить конструктор, с вызовом родительского конструктора. Определить
    функции добавления новой песни, удаления песни, форматированной печати плейлиста. Переопределить метод
    преобразования в строку для печати основной информации (исполнитель, название альбома, жанр,
    студия звукозаписи, цена).
Создать производный от Disk класс DVD. Новые поля: режиссер, кинокомпания, главные роли (словарь вида роль: ФИ актера).
    Определить конструктор, с вызовом родительского конструктора. Определить функции изменения режиссера, добавления,
    удаления и изменения списка главных ролей. Переопределить метод преобразования в строку для печати основной
    информации (режиссер, название фильма, жанр, кинокомпания, цена).
Создать класс Store. Поля: название магазина, адрес, коллекция аудиодисков (список экземпляров класса Audio),
    коллекция фильмов (список экземпляров класса DVD). Определить конструктор. Переопределить метод преобразования
    в строку для печати всей информации о магазине (с использованием переопределения в классах Audio и DVD).
    Переопределить методы получения количества дисков функцией len, получения диска по индексу, изменения по
    индексу, удаления по индексу (пусть вначале идут индексы аудиодисков, затем фильмов). Переопределить
    операции + и - для добавления или удаления диска. Добавить функцию создания txt-файла и записи всей
    информации в него (в том числе списков песен и главных ролей фильма).
Предусмотреть хотя бы в 3 местах обработку возможных исключений.
В каждом модуле провести подробное тестирование всех создаваемых объектов и функций.
"""


from audio import Audio
from dvd import DVD
class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.audio_collection = []
        self.dvd_collection = []
    def __str__(self):
        s = f"{self.name}\n{self.address}\n\nAudio collection:\n"
        for audio in self.audio_collection:
            s += str(audio) + "\n"
        s += "\nDVD collection:\n"
        for dvd in self.dvd_collection:
            s += str(dvd) + "\n"
        return s
    def __len__(self):
        return len(self.audio_collection) + len(self.dvd_collection)
    def __getitem__(self, index):
        if index < len(self.audio_collection):
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
    def add_disk(self, disk):
        if isinstance(disk, Audio):
            self.audio_collection.append(disk)
        elif isinstance(disk, DVD):
            self.dvd_collection.append(disk)
        else:
            raise TypeError("The disk must be an instance of Audio or DVD")
    def remove_disk(self, disk):
        if isinstance(disk, Audio):
            if disk in self.audio_collection:
                self.audio_collection.remove(disk)
            else:
                raise ValueError("The audio disk is not in the collection")
        elif isinstance(disk, DVD):
            if disk in self.dvd_collection:
                self.dvd_collection.remove(disk)
            else:
                raise ValueError("The DVD disk is not in the collection")
        else:
            raise TypeError("The disk must be an instance of Audio or DVD")
    def create_txt_file(self, filename):
        with open(filename, "w") as f:
            f.write(f"{self.name}\n{self.address}\n\nAudio collection:\n")
            for audio in self.audio_collection:
                f.write(str(audio) + "\n")
                f.write("Songs:\n")
                for song, duration in audio.songs.items():
                    f.write(f"{song} - {duration}\n")
            f.write("\nDVD collection:\n")
            for dvd in self.dvd_collection:
                f.write(str(dvd) + "\n")
                f.write("Roles:\n")
                for role, actor in dvd.roles.items():
                    f.write(f"{role} - {actor}\n")

