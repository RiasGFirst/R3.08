from Point import Point

class Rectangle:
    """
    Class Rectangle
    """

    def __init__(self, point_hd: Point = None, point_bg=Point(), longueur_x : float = 1, longueur_y : float = 1):
        """
        Constructor
        """
        if not isinstance(longueur_x, (int, float)) or not isinstance(longueur_y, (int, float)):
            raise TypeError("Les longueurs doivent être de type int ou float")
        if longueur_x < 0 or longueur_y < 0:
            raise ValueError("Les longueurs doivent être positives")
        if not isinstance(point_bg, Point) or point_hd is not None and not isinstance(point_hd, Point):
            raise TypeError("Les points doivent être de type Point")

        if point_hd is None and longueur_x is not None and longueur_y is not None:
            self._point_hd = Point(longueur_x, longueur_y)

        if point_hd is not None:
            self._point_hd = point_hd

        self._point_bg = point_bg

    def __calculate_length(self) -> float:
        """
        calculate the length of the rectangle
        :return: float
        """
        return self._point_hd.getX() - self._point_bg.getX()

    def __calculate_width(self) -> float:
        """
        calculate the width of the rectangle
        :return: float
        """
        return self._point_hd.getY() - self._point_bg.getY()

    def surface(self) -> float:
        """
        Calculate the surface of the rectangle
        :return: float
        """
        return self.__calculate_length() * self.__calculate_width()

    def perimeter(self) -> float:
        """
        Calculate the perimeter of the rectangle
        :return: float
        """
        return 2 * (self.__calculate_length() + self.__calculate_width())

    def getPoints(self) -> str:
        """
        Return the 4 points of the rectangle
        :return: str
        """
        return f"bas gauche: ({self._point_bg.getX()}, {self._point_bg.getY()}), bas droit: ({self._point_hd.getX()}, {self._point_bg.getY()}), haut gauche: ({self._point_bg.getX()}, {self._point_hd.getY()}), haut droit: ({self._point_hd.getX()}, {self._point_hd.getY()})"

    def pointDansRectangle(self, point: Point) -> bool:
        """
        Check if a point is in the rectangle
        :param point: Point
        :return: bool
        """
        return self._point_bg.getX() <= point.getX() <= self._point_hd.getX() and self._point_bg.getY() <= point.getY() <= self._point_hd.getY()

    def __str__(self) -> str:
        """
        Return the string representation of the rectangle
        :return: str
        """
        return f"""
Rectangle:
    - longueur: {self.__calculate_length()}
    - largeur: {self.__calculate_width()}
    - surface: {self.surface()}
    - perimetre: {self.perimeter()}
    - points: {self.getPoints()}
                """

