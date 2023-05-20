# Создать производный от Disk класс DVD. Новые поля: режиссер, кинокомпания, главные роли (словарь вида роль: ФИ актера).
#     Определить конструктор, с вызовом родительского конструктора. Определить функции изменения режиссера, добавления,
#     удаления и изменения списка главных ролей. Переопределить метод преобразования в строку для печати основной
#     информации (режиссер, название фильма, жанр, кинокомпания, цена).

import pickle
from disk import Disk

class DVD(Disk):
    def __init__(self, name, genre, price, director, company):
        super().__init__(name, genre, price)
        self.director = director
        self.company = company
        self.roles = {}
        self.log_event("CRE", f"Создан объект |{name}| класса DVD")

    def change_director(self, director):
        self.director = director
        self.log_event("INF", f"Режиссер |{self.name}| был изменён на |{director}|")

    def add_role(self, role, actor):
        self.roles[role] = actor
        self.log_event("INF", f"В |{self.name}| была добавлена роль |{role}| актёра |{actor}|")

    def remove_role(self, role):
        if role in self.roles:
            del self.roles[role]
            self.log_event("INF", f"Из |{self.name}| была убрана роль |{role}|")
        # else:
        #     raise ValueError(f"{role} отсутствует в списке ролей")

    def change_role(self, role, actor):
        if role in self.roles:
            self.roles[role] = actor
            self.log_event("INF", f"В |{self.name}| была изменена роль |{role}|")
        # else:
        #     raise ValueError(f"{role} отсутствует в списке ролей")

    def print_roles(self):
        print(f"Роли:")
        for role, actor in self.roles.items():
            print(f"{role} - {actor}")
            self.log_event("INF", f"Вывод всех ролей и актёров из |{self.name}|")

    # def print_playlist(self):
    #     print(f"Плейлист альбома {self.name}:")
    #     for song, duration in self.songs.items():
    #         print(f"{song} - {duration}")

    def __str__(self):
        return f"{self.director} - {self.name} ({self.genre}, {self.company}) - {self.price}$"

def dvd_test():
    Dvd1 = DVD("Евангелион", "Шиза", 15.99, "Хидэаки Анно", "TV Tokyo")
    Dvd1.add_role("Арбуз", "Кадзи")
    Dvd1.add_role("Куртизанка", "Аска")
    try:
        Dvd1.remove_role("Недопонятый гений")
        Dvd1.change_role("Арбуз", "Мисато")
    except AssertionError:
        print("Test Error")
    else:
        print("Test Passed")
        Dvd1.print_roles()


dvd_test()

# Создаем экземпляры класса Person

# Dvd1 = DVD("Евангелион", "Шиза", 15.99, "Хидэаки Анно", "TV Tokyo")
# Dvd1.add_role("Арбуз", "Кадзи")
# Dvd1.add_role("Куртизанка", "Аска")

#
# # Сериализуем экземпляры в файл
# with open("dvds.pkl", "wb") as f:
#     pickle.dump([Dvd1], f)


# song1 = Audio("Single", "Rap", "15", "IVOXYGEN", "SonyJP")
# song1.add_song("Atlantic Ice", "2:32")
# song1.print_playlist()
# print(song1)
# song1.delete_song("Atlantic Ice")
# song1.print_playlist()

