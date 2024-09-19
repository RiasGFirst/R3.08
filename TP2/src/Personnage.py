

class Personnage:
    """
    Classe Personnage
    """
    def __init__(self, pseudo: str, niveau: float = 1):
        """
        Constructeur de la classe Personnage
        :param pseudo:
        :param niveau:
        """
        self.__pseudo = pseudo
        self.__niveau = niveau
        self.__pv = niveau
        self.__initiative = niveau

    def get_pseudo(self)->str:
        """
        Retourne le pseudo du personnage
        :return:
        :rtype: str
        """
        return self.__pseudo

    def get_niveau(self)->float:
        """
        Retourne le niveau du personnage
        :return:
        :rtype: float
        """
        return self.__niveau

    def get_pv(self)->float:
        """
        Retourne les points de vie du personnage
        :return:
        :rtype: float
        """
        return self.__pv

    def get_initiative(self):
        """
        Retourne l'initiative du personnage
        :return:
        :rtype: float
        """
        return self.__initiative

    def set_niveau(self, niveau: float):
        """
        Modifie le niveau du personnage
        :param niveau:
        :return:
        """
        self.__niveau = niveau

    def set_initiative(self, initiative: float):
        """
        Modifie l'initiative du personnage
        :param initiative:
        :return:
        """
        self.__initiative = initiative

    def set_pv(self, pv: float):
        """
        Modifie les points de vie du personnage
        :param pv:
        :return:
        """
        if pv < 0:
            pv = 0
        self.__pv = pv

    def __attaque(self, p: "Personnage"):
        """
        Attaque un personnage
        :param p:
        :return:
        """
        if self.__initiative > p.get_initiative():
            p.set_pv(pv=p.get_pv()-self.degats())
            if p.__pv > 0:
                self.set_pv(self.get_pv()-p.degats())
        elif self.__initiative < p.get_initiative():
            self.set_pv(pv=self.get_pv()-p.degats())
            if self.__pv > 0:
                p.set_pv(p.get_pv()-self.degats())
        else:
            p.set_pv(p.get_pv()-self.degats())
            self.set_pv(self.get_pv()-p.degats())

    def combat(self, p: "Personnage")->str:
        """
        Combat un personnage
        :param p:
        :return:
        :rtype: str
        """
        print(f"{self.get_pseudo()} ({self.get_pv()}) vs {p.get_pseudo()} ({p.get_pv()})")
        while self.__pv > 0 and p.get_pv() > 0:
            self.attaque(p)
            print(f"{self.get_pseudo()} ({self.get_pv()})")
            print(f"{p.get_pseudo()} ({p.get_pv()})")

        if self.__pv > 0:
            return self.__pseudo
        else:
            return p.get_pseudo()

    def soigner(self, p: "Personnage" = None):
        """
        Soigne un personnage
        :param p:
        :return:
        """
        if p is None:
            self.set_pv(self.get_niveau())
        else:
            p.set_pv(p.get_niveau())

    def degats(self)->float:
        """
        Retourne les dégâts du personnage
        :return:
        :rtype: float
        """
        return self.__niveau

    def __eq__(self, other):
        """
        Surcharge de l'opérateur ==
        :param other:
        :return:
        :rtype: bool
        """
        return self.__pseudo == other.__pseudo and self.__niveau == other.get_niveau() and self.__pv == other.get_pv() and self.__initiative == other.get_initiative()


    def __str__(self)->str:
        """
        Surcharge de l'opérateur str
        :return:
        :rtype: str
        """
        return f"""
{self.get_pseudo()} (niv: {self.get_niveau()})
PV: {self.get_pv()}
Initiative: {self.get_initiative()}
"""