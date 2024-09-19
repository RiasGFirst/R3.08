from Personnage import Personnage

class Mage(Personnage):

    def __init__(self, pseudo: str, niveau: float):
        super().__init__(pseudo, niveau)
        self.__mana = niveau*5
        self.set_pv(niveau*5+10)
        self.set_initiative(niveau*6+4)

    def set_mana(self, mana):
        """
        Definir le mana du mage
        :param mana:
        :return:
        """
        self.__mana = mana

    def get_mana(self)->float:
        """
        Recuperer le mana du mage
        :return:
        """
        return self.__mana

    def degats(self) ->float:
        """
        Calculer les degats du mage
        :return:
        """
        if self.get_mana() > 0:
            self.set_mana(self.get_mana()-4)
            return self.get_niveau()+3
        return 0

    def __str__(self):
        return super().__str__() + "Mana: " + str(self.get_mana())