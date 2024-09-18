from Point import Point
import math

class Cercle:
    """
    Classe Cercle
    """
    def __init__(self, rayon: float, centre: Point = Point(0, 0)):
        """
        Constructeur
        """
        self._centre = centre
        self._rayon = rayon

    def getRayon(self)->float:
        """
        Retourne le rayon du cercle
        """
        return self._rayon

    def getCentre(self)->Point:
        """
        Retourne le centre du cercle
        """
        return self._centre

    def diametre(self)->float:
        """
        Retourne le diamètre du cercle
        """
        return 2 * self._rayon

    def perimetre(self)->float:
        """
        Retourne le périmètre du cercle
        """
        return 2 * math.pi * self._rayon

    def surface(self)->float:
        """
        Retourne la surface du cercle
        """
        return math.pi * self._rayon**2

    def intersection(self, cercle: 'Cercle')->bool:
        """
        Retourne True si les deux cercles se coupent, False sinon
        """
        return self._centre.distancePoint(cercle.getCentre()) <= self.diametre()

    def dansCercle(self, point: Point)->bool:
        """
        Retourne True si le point est dans le cercle, False sinon
        """
        return self._centre.distancePoint(point) <= self._rayon

    def __str__(self)->str:
        """
        Retourne une chaîne de caractères représentant le cercle
        """
        return f"Cercle de rayon {self._rayon} et de centre {self._centre}, de diamètre {self.diametre()}, de périmètre {self.perimetre()} et de surface {self.surface()}"  