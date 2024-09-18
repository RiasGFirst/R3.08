
def affiche(text: str) -> None:
    """
    Fonction pour afficher un texte
    :param text:
    :return:
    """
    print(f"texte à afficher: {text}")


class Velo:
    """
    Classe Velo
    """
    def __init__(self, marque: str, taille_pneu: int, couleur: str, nb_vitesse: int) -> None:
        self.marque = marque
        self.taille_pneu = taille_pneu
        self.couleur = couleur
        self.nb_vitesse = nb_vitesse
        self.vitesse_courante = 1

    def gear_up(self) -> int:
        """
        :return:
        :rtype: int
        """
        if self.vitesse_courante < self.nb_vitesse:
            self.vitesse_courante += 1
        return self.vitesse_courante

    def gear_down(self) -> int:
        if self.vitesse_courante > 1:
            self.vitesse_courante -= 1
        return self.vitesse_courante

    def __str__(self) -> str:
        return f"""
Marque: {self.marque}, 
Taille pneu: {self.taille_pneu}, 
Couleur: {self.couleur}, 
Nombre de vitesse: {self.nb_vitesse}, 
Vitesse courante: {self.vitesse_courante}
        """


def principal(str1: str) -> None:
    """
    Fonction principale
    :param str1:
    :return:
    """
    affiche(str1)
    v1 = Velo("Ricoh", 28, "rouge", 7)
    print(v1)
    v1.gear_up()
    print(v1)
    v1.gear_up()
    print(v1)
    v1.gear_down()
    print(v1)


if __name__ == "__main__":
    principal("Bonjour")