from Personnage import Personnage

class Soigneur(Personnage):
    """
    Classe Soigneur
    """
    def __init__(self, pseudo, niveau):
        """
        Creation d'un soigneur
        :param pseudo:
        :param niveau:
        """
        super().__init__(pseudo, niveau)
        self.__heal = 3 * niveau


    def soigner(self, p: "Personnage" = None):
        """
        Soigne un personnage
        :param p:
        :return:
        """
        pv = self.get_pv() + self.__heal
        p.set_pv(pv, is_heal=True)
        return f"{p.get_pseudo()} a été soigné de {pv} points de vie"