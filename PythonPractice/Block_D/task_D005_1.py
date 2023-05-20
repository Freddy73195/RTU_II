import pickle
from audio import Audio
from dvd import DVD
from store import Store

with open("audios.pkl", "rb") as f:
    Songs = pickle.load(f)

for Song1 in Songs:
    print(Song1)
    Song1.print_playlist()
    print('/' * 30)
    Song1.add_song("Столярка", "3:15")
    print(Song1)
    Song1.print_playlist()
    print('/' * 30)
    Song1.remove_song("Чебурашка")
    print(Song1)
    Song1.print_playlist()
    print('/' * 30)


with open("dvds.pkl", "rb") as f:
    Dvds = pickle.load(f)

for Dvd1 in Dvds:
    print(Dvd1)
    Dvd1.print_roles()
    print('/' * 30)
    Dvd1.add_role("Недопонятый гений", "Каору")
    print(Dvd1)
    Dvd1.print_roles()
    print('/' * 30)
    Dvd1.remove_role("Куртизанка")
    print(Dvd1)
    Dvd1.print_roles()
    print('/' * 30)

with open("stores.pkl", "rb") as f:
    Stores = pickle.load(f)

for Store1 in Stores:
    print(Store1)
    print('/' * 30)