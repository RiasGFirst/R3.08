from random import randint

from Tasse import Tasse

def create_tasse():
    color = ["red", "blue", "green"]
    marque = ["starbucks", "nespresso", "Ricoh"]
    contenu = ["cafe", "the", "eau"]
    for i in range(3):
        tasse = Tasse(color[i], randint(25, 150), marque[i])
        print(tasse)
        tasse.remplir(contenu[randint(0, 2)])
        tasse.boire()

create_tasse()

