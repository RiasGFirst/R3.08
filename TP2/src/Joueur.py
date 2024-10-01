from Personnage import Personnage


class Joueur:
    """
    Classe Joueur
    """
    def __init__(self, nom, max_personnages):
        """
        Constructeur de la classe Joueura
        :param nom:
        :param max_personnages:
        """
        self.__nom = nom
        self.__personnages = []
        self.__max_personnages = max_personnages

    def get_nom(self)->str:
        """
        Retourne le nom du joueur
        :return:
        :rtype: str
        """
        return self.__nom

    def add_personnage(self, personnage) -> str:
        """
        Ajoute un personnage à la liste des personnages du joueur
        :param personnage:
        :return:
        """
        if len(self.__personnages) < self.__max_personnages:
            self.__personnages.append(personnage)
            return f"{personnage.get_pseudo()} a été ajouté à la liste des personnages de {self.__nom}"
        else:
            return f"Le joueur {self.__nom} a déjà atteint le nombre maximum de personnages"

    def select_personnage(self, nb: int = None, pseudo: str = None, personnage: Personnage = None) -> Personnage:
        """
        Sélectionne un personnage par son pseudo
        :param nb:
        :param pseudo:
        :param personnage:
        :return:
        """
        if nb is not None:
            if nb <= len(self.__personnages):
                return self.__personnages[nb]
        elif pseudo is not None:
            for p in self.__personnages:
                if p.get_pseudo() == pseudo:
                    return p
        elif personnage is not None:
            for p in self.__personnages:
                if p == personnage:
                    return p
        else:
            return None

    def remove_personnage(self, nb: int = None, pseudo: str = None, personnage: Personnage = None) -> str:
        """
        Supprime un personnage de la liste des personnages du joueur
        :param nb:
        :param pseudo:
        :param personnage:
        :return:
        :rtype: str
        """
        if nb is not None:
            if nb <= len(self.__personnages):
                self.__personnages.pop(nb)
                return f"Personnage {nb} supprimé"
        elif pseudo is not None:
            for p in self.__personnages:
                if p.get_pseudo() == pseudo:
                    self.__personnages.remove(p)
                    return f"Personnage {pseudo} supprimé"
        elif personnage is not None:
            for p in self.__personnages:
                if p == personnage:
                    self.__personnages.remove(p)
                    return f"Personnage {personnage.get_pseudo()} supprimé"


    def __str__(self):
        """
        Surcharge de l'opérateur str
        :return:
        :rtype: str
        """
        personnage = ""

        for p in self.__personnages:
            personnage += f"    - {p.afficher()}\n"

        return f"""
Joueur {self.__nom} possède {len(self.__personnages)} personnage(s)
 
Liste des personnages:
{personnage}
"""
