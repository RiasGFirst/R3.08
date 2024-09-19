from Personnage import Personnage

class Guerrier(Personnage):

    def __init__(self, pseudo: str, niveau: float):
        super().__init__(pseudo, niveau)
        self.set_pv(niveau*8+4)
        self.set_initiative(niveau*4+6)

    def degats(self) ->float:
        """
        Renvoie les dégats du guerrier
        :return:
        :rtype: float
        """
        return self.get_niveau()*2