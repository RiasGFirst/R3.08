class Point:
    """
    Classe Point
    """
    def __init__(self, x: float = 0, y: float = 0):
        """
        Constructeur de la classe Point
        :param x:
        :param y:
        """
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Les coordonnées doivent être des nombres")
        self._x = x
        self._y = y

    def getX(self) -> float:
        """
        Retourne la coordonnée x du point
        :return: float
        """
        return self._x

    def getY(self) -> float:
        """
        Retourne la coordonnée y du point
        :return: float
        """
        return self._y

    def distanceCoordonnees(self, x: float, y: float) -> float:
        """
        Calcule la distance entre le point et un autre point
        :param x: float
        :param y: float
        :return: float
        """
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Les coordonnées doivent être des nombres")
        
        distance = ((self._x-x)**2 + (self._y-y)**2)**0.5
        return distance

    def distancePoint(self, point) -> float:
        """
        Calcule la distance entre le point et un autre point
        :param point: Point
        :return: float
        """
        if not isinstance(point, Point):
            raise TypeError("Le point doit être une instance de la classe Point")

        return self.distanceCoordonnees(point.getX(), point.getY())

    def __str__(self) -> str:
        return f"({self._x}, {self._y})"