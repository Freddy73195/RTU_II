# Создать производный от Disk класс Audio. Новые поля: исполнитель, студия звукозаписи, список песен (словарь вида
#     название песни: длительность). Определить конструктор, с вызовом родительского конструктора. Определить
#     функции добавления новой песни, удаления песни, форматированной печати плейлиста. Переопределить метод
#     преобразования в строку для печати основной информации (исполнитель, название альбома, жанр,
#     студия звукозаписи, цена).


# class Audio(Disk):
#     _all = []
#     def __init__(self, agent, studio, song_list: {}, duration, name, genre, price) -> None:
#         super().__init__(name, genre, price)
#         self.agent = agent
#         self.studio = studio
#         self.song_list = song_list
#         self.duration = duration
#         # self.spisok, self.duration = spisok, duration
#         # self._all.append(self)
#
#         def add_track(self, song_list, )

# class Audio(Disk):
#     def __init__(self, name, genre, price, artist, recording_studio, song_list={}):
#         super().__init__(name, genre, price)
#         self.artist = artist
#         self.recording_studio = recording_studio
#         self.song_list = song_list
#
#     def add_song(self, name, duration):
#         self.song_list[name] = duration
#
#     def delete_song(self, name):
#         if name in self.song_list:
#             del self.song_list[name]
#         else:
#             print(f"Song {name} not found in the playlist.")
#
#     def print_playlist(self):
#         print(f"Playlist for {self.artist} - {self.name}")
#         for song, duration in self.song_list.items():
#             print(f"{song}: {duration}")
#
#     def __str__(self):
#         return f"Artist: {self.artist}\nAlbum Name: {self.name}\nGenre: {self.genre}\nRecording Studio: {self.recording_studio}\nPrice: {self.price}$"
#
# song1 = Audio("Single", "Single", "15", "IVOXYGEN", "SonyJP")
# song1.add_song("Atlantic Ice", "2:32")
# song1.print_playlist()
# print(song1)
# song1.delete_song("Atlantic Ice")
# song1.print_playlist()


import pickle
from disk import Disk
class Audio(Disk):
    def __init__(self, name, genre, price, artist, studio):
        super().__init__(name, genre, price)
        self.artist = artist
        self.studio = studio
        self.songs = {}
        self.log_event("CRE", f"Создан объект |{name}| класса Audio")

    def add_song(self, name, duration):
        self.songs[name] = duration
        self.log_event("INF", f"Добавлена песня |{self.songs}| в альбом |{self.name}|")
    def remove_song(self, name):
        if name in self.songs:
            del self.songs[name]
            self.log_event("INF", f"Удалена песня |{self.songs}| из альбома |{self.name}|")
        else:
            raise ValueError(f"{name} нет в списке")

    def print_playlist(self):
        print(f"Плейлист альбома {self.name}:")
        for song, duration in self.songs.items():
            print(f"{song} - {duration}")
            self.log_event("INF", f"Вывод всех песен из альбома |{self.name}|")
    def __str__(self):
        return f"{self.artist} - {self.name} ({self.genre}, {self.studio}) - {self.price}$"

def audio_test():
    Song1 = Audio("Река крови", "Реп", 10.99, "Кровосток", "KRGP")
    Song1.add_song("Чебурашка", "4:15")
    Song1.add_song("Биография", "3:30")
    try:
        Song1.remove_song("Чебурашка")
        Song1.add_song("Столярка", "3:30")
    except AssertionError:
        print("Test Error")
    else:
        print("Test Passed")
    print(Song1)
    Song1.print_playlist()

audio_test()

# # Создаем экземпляры класса Person
# Song1 = Audio("Река крови", "Реп", 10.99, "Кровосток", "KRGP")
# Song1.add_song("Чебурашка", "4:15")
# Song1.add_song("Биография", "3:30")
#
# # Сериализуем экземпляры в файл
# with open("audios.pkl", "wb") as f:
#     pickle.dump([Song1], f)

    # song1 = Audio("Single", "Rap", "15", "IVOXYGEN", "SonyJP")
    # song1.add_song("Atlantic Ice", "2:32")
    # song1.print_playlist()
    # print(song1)
    # song1.delete_song("Atlantic Ice")
    # song1.print_playlist()