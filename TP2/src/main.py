from sphinx.util.docutils import switch_source_input

from Soigneur import Soigneur
from Guerrier import Guerrier
from random import randint
from Joueur import Joueur
from Mage import Mage
import requests


def main():
    nom = input("Entrez votre nom: ")
    nb_personnages = randint(randint(1, 10), randint(11, 20))
    joueur = Joueur(nom=nom, max_personnages=nb_personnages)

    for i in range(nb_personnages):
        response = requests.get("https://api.namefake.com/english-united-states/female/")
        if response.ok:
            data = response.json()
            nom = data["name"]
            choix = randint(1, 3)
            niveau = randint(1, 100)
            match choix:
                case 1:
                    joueur.add_personnage(Soigneur(pseudo=nom, niveau=niveau))
                case 2:
                    joueur.add_personnage(Guerrier(pseudo=nom, niveau=niveau))
                case 3:
                    joueur.add_personnage(Mage(pseudo=nom, niveau=niveau))
                case _:
                    print("Erreur lors de la création du personnage")

        else:
            return "Erreur lors de la récupération du nom"

    print(joueur)



if __name__ == "__main__":
    main()