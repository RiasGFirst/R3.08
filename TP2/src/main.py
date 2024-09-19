from Guerrier import Guerrier
from Joueur import Joueur
from Mage import Mage

def main():
    j = Joueur("Joueur 1", 2)
    g = Guerrier("Guerrier 1", 10)
    m = Mage("Mage 1", 10)
    print(j.add_personnage(g))
    print(j.add_personnage(m))
    print(j.add_personnage(Mage("Mage 2", 10)))

    print(j.select_personnage(nb=1))
    print(j.select_personnage(pseudo="Mage 1"))
    print(j.select_personnage(personnage=g))

    print(j.remove_personnage(nb=1))
    print(j.remove_personnage(pseudo="Guerrier 1"))


if __name__ == "__main__":
    main()