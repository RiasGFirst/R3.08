from Point import Point

class Triangle:

    def __init__(self, longueur: float, largeur: float, angle_droit: Point = Point):
        """
        :param longueur:
        :param largeur:
        :param angle_droit:
        """
        if not isinstance(longueur, (int, float)):
            raise ValueError("La longueur doit être un nombre")
        if not isinstance(largeur, (int, float)):
            raise ValueError("La largeur doit être un nombre")
        if not isinstance(angle_droit, Point):
            raise ValueError("L'angle droit doit être un point")

        self._longueur = longueur
        self._largeur = largeur
        self._angle_droit = angle_droit

    def hypothenuse(self) -> float:
        """
        Calculate the hypothenuse of the triangle
        :return: float
        """
        return (self._longueur ** 2 + self._largeur ** 2) ** 0.5

    def perimetre(self) -> float:
        """
        Calculate the perimeter of the triangle
        :return: float
        """
        return self._longueur + self._largeur + self.hypothenuse()

    def surface(self) -> float:
        """
        Calculate the surface of the triangle
        :return: float
        """
        return self._longueur * self._largeur / 2

    def isisocele(self) -> bool:
        """
        Check if the triangle is isosceles
        :return: boolean
        """
        return self._longueur == self._largeur or self._longueur == self.hypothenuse() or self._largeur == self.hypothenuse()

    def __str__(self) -> str:
        """
        :return: str
        """
        return f"Triangle de longueur {self._longueur}, de largeur {self._largeur}, d'angle droit {self._angle_droit}."